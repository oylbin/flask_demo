from flask_login import UserMixin


class DemoUser(UserMixin):

    def __init__(self, _id):
        self.id = _id
