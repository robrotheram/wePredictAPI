__author__ = 'robert'
from flask import Flask

app = Flask(__name__)

import wePredictAPI.views
import wePredictAPI.views.v1.Asmtha

