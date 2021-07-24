from flask import Blueprint, g, render_template, request, flash, redirect, url_for
import psycopg2
from . import db
import datetime as dt

auth = Blueprint('auth', __name__)


@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        conn = db.get_db()
        cur = conn.cursor()
        username = request.form.get('inputuser')
        email = request.form.get('inputEmail')
        password = request.form.get('inputPassword')
        check = request.form.get('inputPasswordcheck')
        cur.execute(
            "select (email) from details where username=%s", (username,))
        ee = cur.fetchall()
        if ee:
            flash('Username already exists', category='error')
            return redirect(url_for('auth.signup'))
        if password != check:
            flash('Password not matches.', category='error')
            return redirect(url_for('auth.signup'))
        elif not (username and email):
            flash('Enter all feilds.', category='error')
            return redirect(url_for('auth.signup'))
        else:
            date = dt.date.today()
            flash('Account created successfully, you can login now',
                  category='success')

            cur.execute('insert into details(username,email,password,updated) values (%s,%s,%s,%s)',
                        (username, email, password, date))
            conn.commit()
            cur.close()
            return redirect(url_for("auth.login"))
    return render_template("signup.html")


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('inputuser')
        password = request.form.get('inputPassword')
        conn = db.get_db()
        cur = conn.cursor()
        cur.execute(
            "select (password) from details where username = %s", (username,))
        passi = cur.fetchall()
        if not passi:
            flash('No username found, try signin', category='error')
            return redirect(url_for('auth.signup'))
        for p in passi:
            if password == p[0]:
                return redirect(url_for("auth.todo", user=username))
            else:
                flash('Password not correct.', category='error')
                return redirect(url_for('auth.login'))
        cur.close()
    return render_template("login.html")


@auth.route("/<user>", methods=['GET', 'POST'])
def todo(user):
    conn = db.get_db()
    cur = conn.cursor()
    if request.method == 'GET':
        cur.execute(
            "select notes,time from notes where usr in (select (id) from details where username= %s)", (user,))
        lis = cur.fetchall()
        cur.close()
        date = dt.date.today()
        return render_template("todo.html", lists=lis)
    if request.method == 'POST':
        note = request.form.get('task')
        date = request.form.get('date')
        dat = dt.date.today()
        if not (note and date):
            flash("Enter task and date.", category='error')
            return redirect(url_for("auth.todo", user=user))
        cur.execute("select id from details where username=%s", (user,))
        id = cur.fetchone()
        cur.execute(
            "insert into notes(notes,time,usr) values (%s,%s,%s)", (note, date, id,))
        conn.commit()
        cur.close()
        return redirect(url_for('auth.todo', user=user))
