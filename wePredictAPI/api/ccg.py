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
                          "AVG(2009_COPD_QOF_Value) as 2009_COPD, "
                          "AVG(2010_COPD_QOF_Value) as 2010_COPD,"
                          "AVG(2011_COPD_QOF_Value) as 2011_COPD,"
                          "AVG(2012_COPD_QOF_Value) as 2012_COPD,"
                          "AVG(2013_COPD_QOF_Value) as 2013_COPD, "
                          "AVG(2009_Asthma_Value) as 2009_ASTHMA,"
                          "AVG(2010_Asthma_Value) as 2010_ASTHMA,"
                          "AVG(2011_Asthma_Value) as 2011_ASTHMA, "
                          "AVG(2012_Asthma_Value) as 2012_ASTHMA, "
                          "AVG(2012_smoking_prevalence_Value) as 2012_SMOKING ,"
                          "AVG(2013_smoking_prevalence_Value) as 2013_SMOKING,"
                          "AVG(2010_flu_vaccine_65_Value) as 2010_FLU65, "
                          "AVG(2010_flu_vaccine_06_Value) as 2010_FLU06  "
                          "FROM TBL_PRACTICE_DATA "
                          "join TBL_PRACTICE_INFO on TBL_PRACTICE_DATA.Practice_Code = TBL_PRACTICE_INFO.Practice_Code "
                          "group by CCG_Name;")
    return data, 200, {'Access-Control-Allow-Origin': '*'}

class CCG_Asmatha_ALL(Resource):
  "My TODO API"
  @swagger.operation(
      notes='Get Heatmap data',
      nickname='get',
    )
  def get(self):
    """Get heat map infomation
    """
    data = g.db.getResult("SELECT CCG_Name, "
                          "AVG(2009_Asthma_Value) as 2009_ASTHMA,"
                          "AVG(2009_Asthma_Upper) as 2009_ASTHMA_Upper,"
                          "AVG(2009_Asthma_Lower) as 2009_ASTHMA_Lower,"
                          "AVG(2010_Asthma_Value) as 2010_ASTHMA,"
                          "AVG(2010_Asthma_Upper) as 2010_Asthma_Upper,"
                          "AVG(2010_Asthma_Lower) as 2010_Asthma_Lower,"
                          "AVG(2011_Asthma_Value) as 2011_ASTHMA,"
                          "AVG(2011_Asthma_Upper) as 2011_ASTHMA_Upper,"
                          "AVG(2011_Asthma_Lower) as 2011_ASTHMA_Lower,"
                          "AVG(2012_Asthma_Value) as 2012_ASTHMA,"
                          "AVG(2012_Asthma_Upper) as 2012_Asthma_Upper,"
                          "AVG(2012_Asthma_Lower) as 2012_Asthma_Lower "
                          "FROM TBL_PRACTICE_INFO "
                          "join TBL_PRACTICE_DATA on TBL_PRACTICE_INFO.Practice_Code = TBL_PRACTICE_DATA.Practice_Code "
                          "group by CCG_Name;")
    return data, 200, {'Access-Control-Allow-Origin': '*'}

class CCG_Asmatha(Resource):
  "My TODO API"
  @swagger.operation(
      notes='Get Heatmap data',
      nickname='get',
    )
  def get(self,ccg_id):
    """Get Data of a specific Practice in CCG
    """
    ccg = urllib.unquote(ccg_id)
    data = g.db.getResult("SELECT CCG_Name, "
                          "AVG(2009_Asthma_Value) as 2009_ASTHMA,"
                          "AVG(2009_Asthma_Upper) as 2009_ASTHMA_Upper,"
                          "AVG(2009_Asthma_Lower) as 2009_ASTHMA_Lower,"
                          "AVG(2010_Asthma_Value) as 2010_ASTHMA,"
                          "AVG(2010_Asthma_Upper) as 2010_Asthma_Upper,"
                          "AVG(2010_Asthma_Lower) as 2010_Asthma_Lower,"
                          "AVG(2011_Asthma_Value) as 2011_ASTHMA,"
                          "AVG(2011_Asthma_Upper) as 2011_ASTHMA_Upper,"
                          "AVG(2011_Asthma_Lower) as 2011_ASTHMA_Lower,"
                          "AVG(2012_Asthma_Value) as 2012_ASTHMA,"
                          "AVG(2012_Asthma_Upper) as 2012_Asthma_Upper,"
                          "AVG(2012_Asthma_Lower) as 2012_Asthma_Lower "
                          "FROM TBL_PRACTICE_INFO "
                          "join TBL_PRACTICE_DATA on "
                          "TBL_PRACTICE_INFO.Practice_Code = TBL_PRACTICE_DATA.Practice_Code "
                          "where CCG_NAME = %s "
                          "group by CCG_NAME;",(ccg_id))
    return data, 200, {'Access-Control-Allow-Origin': '*'}