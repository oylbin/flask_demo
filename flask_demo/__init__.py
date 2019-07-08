import os
from flask import Flask

from . import routes

from .services import loginservice
from . import commands


def create_app():
    app = Flask(__name__)

    from . import default_settings
    app.config.from_object(default_settings)

    # load config from config file
    #  the value of FLASK_DEMO_SETTINGS_FILE should be
    #  the absolute path name of the config file
    app.config.from_envvar('FLASK_DEMO_SETTINGS_FILE', True)

    # load config from ENV
    # when using docker-compose, EVNs are defined in docker-compose.yml
    # the configuration priority: ENV > config file > default settings
    for key in dir(default_settings):
        if key.isupper():
            app.config[key] = os.getenv(key, app.config[key])

    app.register_blueprint(routes.bp, url_prefix='/')
    loginservice.init_app(app, {'flask_demo': '/signin'})
    commands.init_commands(app)
    return app
