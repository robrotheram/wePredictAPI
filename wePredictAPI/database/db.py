__author__ = 'robertfletcher'
## @package wePredictAPI.database.db
#  API Classes that are specific to Database connections

from flask import g
from wePredictAPI.settings import *
import PySQLPool

## Defines the Global Connection Pool of Database connections
connection = PySQLPool.getNewConnection(username=username, password=password, host=hostname, db=database)

class DB(object):

    def __init__(self):
        """
        """

    def getResultParamaters(self,sql_query,values):
        """
        Get result form database when SQL query and values statement
        :param sql_query: SQL Query
        :param values: Vales to be inserted into the query before being run
        :return data: Object Array of the results
        """

        query = PySQLPool.getNewQuery(connection)
        query.Query(sql_query,values)
        data = query.record
        return data

    def getResult(self,sql_query):
        """
        Get result form database when SQL query statement
        :param sql_query: SQL Query
        :return data: Object Array of the results
        """
        query = PySQLPool.getNewQuery(connection)
        query.Query(sql_query)
        data = query.record
        return data

