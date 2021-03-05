from flask import render_template, url_for, flash, redirect
from flaskApp import app

@app.route("/")
@app.route("/home")
def home():
    return render_template('index.html')
@app.route("/meditation")
def meditation():
    return render_template('meditation.html')