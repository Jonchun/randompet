from flask import Flask
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:c0sak4jetyo@127.0.0.1:3306/randompet"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy()
ma = Marshmallow()

db.init_app(app)
migrate = Migrate(app, db)

import randompet.commands