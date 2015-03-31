__author__ = 'robert'
from flask import Flask ,g
from flask_cors import CORS
from wePredictAPI.database.db import DB
from flask import Flask, redirect
from flask.ext.restful import reqparse, abort, Api, Resource, fields, marshal_with
from flask_restful_swagger import swagger
import urllib


class CcgList(Resource):
  "My TODO API"
  @swagger.operation(
      notes='Get list of all CCG in England',
      nickname='get',
    )
  def get(self):
    """Get list of all CCG in England
    """
    data = g.db.getResult("SELECT Practice_Code,CCG_Name FROM TBL_PRACTICE_INFO group by CCG_Name;")
    return data, 200, {'Access-Control-Allow-Origin': '*'}

