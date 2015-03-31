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



class HeatMap(Resource):
  "My TODO API"
  @swagger.operation(
      notes='Get Heatmap data',
      nickname='get',
    )
  def get(self):
    """Get list of all CCG in England
    """
    data = g.db.getResult("SELECT CCG_Name, "
                          "sum(2009_COPD_QOF_Value), "
                          "sum(2010_COPD_QOF_Value),"
                          "sum(2011_COPD_QOF_Value),"
                          "sum(2012_COPD_QOF_Value),"
                          "sum(2013_COPD_QOF_Value), "
                          "sum(2009_Asthma_Value),"
                          "sum(2010_Asthma_Value),"
                          "sum(2011_Asthma_Value), "
                          "sum(2012_Asthma_Value), "
                          "sum(2012_smoking_prevalence_Value),"
                          "sum(2013_smoking_prevalence_Value),"
                          "sum(2010_flu_vaccine_65_Value), "
                          "sum(2010_flu_vaccine_06_Value)  "
                          "FROM TBL_PRACTICE_INFO "
                          "join TBL_PRACTICE_DATA on "
                          "TBL_PRACTICE_INFO.Practice_Code = TBL_PRACTICE_DATA.Practice_Code "
                          "group by CCG_Name;")
    return data, 200, {'Access-Control-Allow-Origin': '*'}
