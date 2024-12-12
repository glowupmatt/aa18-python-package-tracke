from flask import Flask
from app.model import db
from flask_migrate import Migrate
from app.config import Config
from .routes import bp
from dotenv import load_dotenv

import os

load_dotenv()


app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
Migrate(app, db)

app.register_blueprint(bp)

if __name__ == "__main__":
    app.run(debug=True)