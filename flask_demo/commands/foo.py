import click

from flask import current_app
from flask.cli import with_appcontext


@click.command('create')
@click.argument('name')
@with_appcontext
def create_user(name):
    # this command can be invoked from cli: "flask create <NAME>"
    print("create user: " + name)
    print(current_app.config)
