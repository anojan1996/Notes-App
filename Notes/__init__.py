from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
db = SQLAlchemy(app)
login_manager = LoginManager(app)


app.config['SECRET_KEY'] = 'Notes'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///notes.db'

login_manager.login_view = 'login'


from Notes import routes


