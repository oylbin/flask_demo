import click

from flask import current_app
from flask.cli import with_appcontext


@click.command('create')
@click.option('--project', default=None, help='project name')
@click.argument('name')
@with_appcontext
def create_user(name, **options):
    # this command can be invoked from cli: "flask create  --project <project> <NAME>"
    print("create user: " + name)
    print(options)
    print(current_app.config)
