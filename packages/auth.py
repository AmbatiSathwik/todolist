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
                return "<h1>Found</h1>"
            else:
                flash('Password not correct.', category='error')
                return redirect(url_for('auth.login'))
        cur.close()
    return render_template("login.html")
