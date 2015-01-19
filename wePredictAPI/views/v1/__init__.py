__author__ = 'robert'
from wePredictAPI import app


@app.route('/')
def index():
    return 'Hello World!'