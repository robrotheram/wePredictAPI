__author__ = 'robertfletcher'
from DBUtils.PooledDB import PooledDB
from wePredictAPI.settings import *
import _mysql

class DB(object):

    def __init__(self):
        self.pool = PooledDB(creator = _mysql,
                mincached = 5,
                db = database,
                host = hostname,
                user = username,
                passwd= password)


    def getConnection(self):
        return self.pool.connection()

    def getResult(self,querry):
        db = self.getConnection()
        cursor = db.cursor()
        cursor.execute(querry)
        db.close()
        return cursor.fetchall()