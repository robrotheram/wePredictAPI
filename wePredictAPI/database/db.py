__author__ = 'robertfletcher'
from flask import g
from wePredictAPI.settings import *
import PySQLPool

connection = PySQLPool.getNewConnection(username=username, password=password, host=hostname, db=database)

class DB(object):

    def __init__(self):
        #g.cnx_pool = pymysql.connector.pooling.MySQLConnectionPool(pool_name="name",
                                                             # pool_size=10,
                                                             # autocommit=True,
                                                             # user=username,
                                                             # password=password,
                                                             # host=hostname,
                                                             # database=database)


    def getConnection(self):
        return self.pool.connection()

    def getResult(self,querry):

        query = PySQLPool.getNewQuery(connection)
        query.QueryOne(querry)
        return query


        #conn = g.cnx_pool.get_connection()
        #cursor = conn.cursor()
        #cursor.execute(querry)
        #db.close()
        #return cursor.fetchall()

