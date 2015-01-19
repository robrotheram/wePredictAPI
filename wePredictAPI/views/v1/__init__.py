__author__ = 'robert'
from flask import render_template

from wePredictAPI import app


@app.route("/")
def hello():
    return render_template('index.html')


@app.route("/chart")
def chartTest():
    return render_template('chart_test.html')