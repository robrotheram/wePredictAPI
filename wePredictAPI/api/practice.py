__author__ = 'robert'

from flask import Flask ,g
from flask_cors import CORS
from wePredictAPI.database.db import DB
from flask import Flask, redirect
from flask.ext.restful import reqparse, abort, Api, Resource, fields, marshal_with
from flask_restful_swagger import swagger
import urllib


class Practice(Resource):
  "My TODO API"
  @swagger.operation(
      notes='Get a Practice in CCG',
      nickname='get',
    )
  def get(self,ccg_id):
    """Get a Practice in CCG
    """
    prac = urllib.unquote(ccg_id)
    qurry = ("SELECT Practice_Name FROM ADRESS join CCG on PracticeCode = CCG.Practice_Code where CCG = '"+prac+"';")
    data = g.db.getResult(qurry)
    return data, 200, {'Access-Control-Allow-Origin': '*'}



class PracticeList(Resource):
  "My TODO API"
  @swagger.operation(
      notes='Get list of all Practice in CCG',
      nickname='get',
    )
  def get(self):
    """Get list of all Practice in CCG
    """
    qurry = ("SELECT Practice_Name FROM ADRESS join CCG on PracticeCode = CCG.Practice_Code ")
    data = g.db.getResult(qurry)
    return data, 200, {'Access-Control-Allow-Origin': '*'}

class PracticeData(Resource):
  "My TODO API"
  @swagger.operation(
      notes='Get Data of a specific Practice in CCG',
      nickname='get',
    )
  def get(self,practice_id):
    """Get Data of a specific Practice in CCG
    """
    practice = urllib.unquote(practice_id)
    qurry = ("select * from TBL_PRACTICE_INFO "
             "JOIN  TBL_PRACTICE_DATA ON TBL_PRACTICE_INFO.Practice_Code = TBL_PRACTICE_DATA.Practice_Code "
             "where Practice_Name = '"+practice+"';")
    data = g.db.getResult(qurry)
    return data, 200, {'Access-Control-Allow-Origin': '*'}
