from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from app.config import Conf


app = Flask(__name__)
app.config.from_object(Conf)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes, models