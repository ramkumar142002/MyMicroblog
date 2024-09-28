from flask.cli import locate_app
from app import app
from app import cli

app = locate_app()

app.app_context().push()
