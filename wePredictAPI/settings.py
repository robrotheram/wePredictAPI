__author__ = 'robertfletcher'
import os

#global database varibles



hostname=os.environ['OPENSHIFT_MYSQL_DB_HOST']
username=os.environ['OPENSHIFT_MYSQL_DB_USERNAME']
password=os.environ['OPENSHIFT_MYSQL_DB_PASSWORD']
database="wePredictV2"
