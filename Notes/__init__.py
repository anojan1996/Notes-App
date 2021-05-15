from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)


app.config['SECRET_KEY'] = 'Notes'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///notes.db'


from Notes import routes


