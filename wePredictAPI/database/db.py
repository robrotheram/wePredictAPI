__author__ = 'robertfletcher'
from flask import g
from DBUtils.PooledDB import PooledDB
from wePredictAPI.settings import *
import MySQLdb

class DB(object):

    def __init__(self):
        g.cnx_pool = PooledDB(creator = MySQLdb,
                pool_name="name",
                pool_size=10,
                autocommit=True,
                db = database,
                host = hostname,
                user = username,
                passwd= password,
                charset = "utf8")


    def getConnection(self):
        return g.cnx_pool.get_connection()

    def getResult(self,querry):
        conn = g.cnx_pool.get_connection()
        cursor = conn.cursor()
        cursor.execute(querry)
        db.close()
        return cursor.fetchall()