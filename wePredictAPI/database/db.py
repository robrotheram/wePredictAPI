__author__ = 'robertfletcher'

import MySQLdb

from wePredictAPI.settings import *


def dbconnect():
    db = MySQLdb.connect(host=hostname, port=3306, user=username, passwd=password, db=database)
    return db


