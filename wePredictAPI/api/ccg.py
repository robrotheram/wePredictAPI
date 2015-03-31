__author__ = 'robert'
from flask import Flask ,g
from flask_cors import CORS
from wePredictAPI.database.db import DB
from flask import Flask, redirect
from flask.ext.restful import reqparse, abort, Api, Resource, fields, marshal_with
from flask_restful_swagger import swagger
import simplejson
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
    """Get heat map infomation
    """
    data = g.db.getResult("SELECT CCG_Name, "
                          "sum(2009_COPD_QOF_Value) as 2009_COPD, "
                          "sum(2010_COPD_QOF_Value) as 2010_COPD,"
                          "sum(2011_COPD_QOF_Value) as 2011_COPD,"
                          "sum(2012_COPD_QOF_Value) as 2012_COPD,"
                          "sum(2013_COPD_QOF_Value) as 2013_COPD, "
                          "sum(2009_Asthma_Value) as 2009_ASTHMA,"
                          "sum(2010_Asthma_Value) as 2010_ASTHMA,"
                          "sum(2011_Asthma_Value) as 2011_ASTHMA, "
                          "sum(2012_Asthma_Value) as 2012_ASTHMA, "
                          "sum(2012_smoking_prevalence_Value) as 2012_SMOKING ,"
                          "sum(2013_smoking_prevalence_Value) as 2013_SMOKING,"
                          "sum(2010_flu_vaccine_65_Value) as 2010_FLU65, "
                          "sum(2010_flu_vaccine_06_Value) as 2010_FLU06  "
                          "FROM TBL_PRACTICE_INFO "
                          "join TBL_PRACTICE_DATA on "
                          "TBL_PRACTICE_INFO.Practice_Code = TBL_PRACTICE_DATA.Practice_Code "
                          "group by CCG_Name;")
    js_data = []
    for obj in data:
        objjst = {
            "CCG_Name": obj['CCG_Name'],
            "2009_COPD": float(obj['2009_COPD']),
            "2010_COPD": float(obj['2010_COPD']),
            "2011_COPD": float(obj['2011_COPD']),
            "2012_COPD": float(obj['2012_COPD']),
            "2013_COPD": float(obj['2013_COPD']),
            "2009_ASTHMA": float(obj['2009_ASTHMA']),
            "2010_ASTHMA": float(obj['2010_ASTHMA']),
            "2011_ASTHMA": float(obj['2011_ASTHMA']),
            "2012_ASTHMA": float(obj['2012_ASTHMA']),
            "2012_SMOKING": float(obj['2012_SMOKING']),
            "2013_SMOKING": float(obj['2013_SMOKING']),
            "2010_FLU65": float(obj['2010_FLU65']),
            "2010_FLU06": float(obj['2010_FLU06'])
            }
        js_data.append(objjst)

    return js_data, 200, {'Access-Control-Allow-Origin': '*'}
