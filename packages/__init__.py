from flask import Flask, render_template
from .auth import auth
from . import db

DATABASE = 'postgres://weyjofmlbnfpsd:f740781f35fc7bdf5421b1c3e30ae7d9eefa09b0dd0f8c3fc8692095b3ea669d@ec2-35-174-122-153.compute-1.amazonaws.com:5432/d5kh8rbolevrrd'
DEBUG = True
SECRET_KEY = 'sathwikisgreat'


def create_app():
    app = Flask(__name__)
    app.config.from_object(__name__)
    app.register_blueprint(auth, url_prefix='/')
    db.init_app(app)
    return app
