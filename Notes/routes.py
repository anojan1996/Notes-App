from Notes import app
from flask import render_template


@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/logout')
def logout():
    return "<p>Logout</p>"

@app.route('/sign-up')
def sign_up():
    return render_template('sign_up.html')