from flask_login import LoginManager
from flask_login import login_user
from ..components.demouser import DemoUser


def init_app(app, blueprint_login_views={}):
    # login_manager 相关代码放在这里是否合适？
    login_manager = LoginManager()
    login_manager.init_app(app)

    login_manager.blueprint_login_views = blueprint_login_views

    @login_manager.user_loader
    def load_user(user_id):
        return DemoUser(user_id)


def login(username, password):
    # FIXME check username & password from database

    user = DemoUser(username)
    login_user(user)
    return True
