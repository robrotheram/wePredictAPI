__author__ = 'robert'
from flask import Flask
from DBUtils.PooledDB import PooledDB
from wePredictAPI.settings import *
import MySQLdb

pool = PooledDB( creator = MySQLdb, mincached = 5, db = database, host = hostname, user = username, passwd= password, charset = "utf8", use_unicode = True)
__db = pool.connection(0)


app = Flask(__name__)

import wePredictAPI.views.v1
import wePredictAPI.views.v1.Asmtha
import wePredictAPI.views.v1.COPD
import wePredictAPI.views.v1.flu
import wePredictAPI.views.v1.MedicalCenters
import wePredictAPI.views.v1.Pollution
import wePredictAPI.views.v1.smoking