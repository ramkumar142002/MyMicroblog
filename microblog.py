from flask.cli import locate_app
from app import app

app = locate_app()

app.app_context().push()
