from flask import Blueprint, g, render_template, request, flash, redirect, url_for
import psycopg2
from . import db

auth = Blueprint('auth', __name__)


@auth.route('/signup', methods=['GET', 'POST'])
def signin():
    return render_template("signup.html")


@auth.route('/login', methods=['GET', 'POST'])
def login():
    return render_template("login.html")
