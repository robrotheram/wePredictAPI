__author__ = 'robert'
from flask import Flask

app = Flask(__name__)

import wePredictAPI.views.v1
import wePredictAPI.views.v1.Asmtha
import wePredictAPI.views.v1.smoking
