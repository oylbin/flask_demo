from . import foo


def init_commands(app):
    app.cli.add_command(foo.create_user)
