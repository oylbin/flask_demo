import os
from flask import Flask

from . import routes

from .services import loginservice
from . import commands


def create_app():
    app = Flask(__name__)

    # hard coded config
    app.config['SECRET_KEY'] = 'this is a secret key'

    # load config from config file

    # load config from ENV
    # when using docker-compose, EVNs are defined in docker-compose.yml
    app.config['mysql_host'] = os.getenv('MYSQL_HOST', '127.0.0.1')
    app.config['mysql_port'] = os.getenv('MYSQL_PORT', 3306)
    app.config['mysql_user'] = os.getenv('MYSQL_USER', 'ga')
    app.config['mysql_password'] = os.getenv('MYSQL_PASSWORD', '4t9wegcvbYSd')
    app.config['mysql_database'] = os.getenv('MYSQL_DATABASE', 'flask_demo')

    app.register_blueprint(routes.bp, url_prefix='/')
    loginservice.init_app(app, {'flask_demo': '/signin'})
    commands.init_commands(app)
    return app
