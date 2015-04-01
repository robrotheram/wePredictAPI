__author__ = 'robert'

from flask import g
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
    data = g.db.getResultParamaters("SELECT Practice_Code,Practice_Name  FROM TBL_PRACTICE_INFO where CCG_Name = \"%s\";",(prac))
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
    data = g.db.getResult("SELECT Practice_Code,Practice_Name FROM TBL_PRACTICE_INFO")
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
    qurry = ("select * from TBL_PRACTICE_DATA where Practice_Code ='"+practice+"' ")
    data = g.db.getResult(qurry)
    return data, 200, {'Access-Control-Allow-Origin': '*'}



class Practice_Asmatha(Resource):
  "My TODO API"
  @swagger.operation(
      notes='Get Heatmap data',
      nickname='get',
    )
  def get(self,practice_id):
    """Get Data of a specific Practice in CCG
    """
    ccg = urllib.unquote(practice_id)
    data = g.db.getResultParamaters("SELECT CCG_Name, "
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
                          "group by CCG_NAME;",(ccg))
    return data, 200, {'Access-Control-Allow-Origin': '*'}

class Practice_COPD_QOF(Resource):
  "My TODO API"
  @swagger.operation(
      notes='Get Heatmap data',
      nickname='get',
    )
  def get(self,practice_id):
    """Get Data of a specific Practice in CCG
    """
    ccg = urllib.unquote(practice_id)
    data = g.db.getResultParamaters("SELECT CCG_Name, "
                          "AVG(2009_COPD_QOF_Value) as 2009_COPD_QOF,"
                          "AVG(2009_COPD_QOF_Upper) as 2009_COPD_QOF_Upper,"
                          "AVG(2009_COPD_QOF_Lower) as 2009_COPD_QOF_Lower,"
                          "AVG(2010_COPD_QOF_Value) as 2010_COPD_QOF,"
                          "AVG(2010_COPD_QOF_Upper) as 2010_COPD_QOF_Upper,"
                          "AVG(2010_COPD_QOF_Lower) as 2010_COPD_QOF_Lower,"
                          "AVG(2011_COPD_QOF_Value) as 2011_COPD_QOF,"
                          "AVG(2011_COPD_QOF_Upper) as 2011_COPD_QOF_Upper,"
                          "AVG(2011_COPD_QOF_Lower) as 2011_COPD_QOF_Lower,"
                          "AVG(2012_COPD_QOF_Value) as 2012_COPD_QOF,"
                          "AVG(2012_COPD_QOF_Upper) as 2012_COPD_QOF_Upper,"
                          "AVG(2012_COPD_QOF_Lower) as 2012_COPD_QOF_Lower, "
                          "AVG(2013_COPD_QOF_Value) as 2013_COPD_QOF,"
                          "AVG(2013_COPD_QOF_Upper) as 2013_COPD_QOF_Upper,"
                          "AVG(2013_COPD_QOF_Lower) as 2013_COPD_QOF_Lower "
                          "FROM TBL_PRACTICE_DATA "
                          "where Practice_Code = %s;",(ccg))
    return data, 200, {'Access-Control-Allow-Origin': '*'}


class Practice_Obesity_QOF(Resource):
  "My TODO API"
  @swagger.operation(
      notes='Get Heatmap data',
      nickname='get',
    )
  def get(self,practice_id):
    """Get Data of a specific Practice in CCG
    """
    ccg = urllib.unquote(practice_id)
    data = g.db.getResultParamaters("SELECT CCG_Name, "
                          "AVG(2009_Obesity_QOF_Value) as 2009_Obesity_QOF,"
                          "AVG(2009_Obesity_QOF_Upper) as 2009_Obesity_QOF_Upper,"
                          "AVG(2009_Obesity_QOF_Lower) as 2009_Obesity_QOF_Lower,"
                          "AVG(2010_Obesity_QOF_Value) as 2010_Obesity_QOF,"
                          "AVG(2010_Obesity_QOF_Upper) as 2010_Obesity_QOF_Upper,"
                          "AVG(2010_Obesity_QOF_Lower) as 2010_Obesity_QOF_Lower,"
                          "AVG(2011_Obesity_QOF_Value) as 2011_Obesity_QOF,"
                          "AVG(2011_Obesity_QOF_Upper) as 2011_Obesity_QOF_Upper,"
                          "AVG(2011_Obesity_QOF_Lower) as 2011_Obesity_QOF_Lower,"
                          "AVG(2012_Obesity_QOF_Value) as 2012_Obesity_QOF,"
                          "AVG(2012_Obesity_QOF_Upper) as 2012_Obesity_QOF_Upper,"
                          "AVG(2012_Obesity_QOF_Lower) as 2012_Obesity_QOF_Lower, "
                          "AVG(2013_Obesity_QOF_Value) as 2013_Obesity_QOF,"
                          "AVG(2013_Obesity_QOF_Upper) as 2013_Obesity_QOF_Upper,"
                          "AVG(2013_Obesity_QOF_Lower) as 2013_Obesity_QOF_Lower "
                          "FROM TBL_PRACTICE_DATA "
                          "where Practice_Code = %s;",(ccg))
    return data, 200, {'Access-Control-Allow-Origin': '*'}

class Practice_CHD_QOF(Resource):
  "My TODO API"
  @swagger.operation(
      notes='Get Heatmap data',
      nickname='get',
    )
  def get(self,practice_id):
    """Get Data of a specific Practice in CCG
    """
    ccg = urllib.unquote(practice_id)
    data = g.db.getResultParamaters("SELECT CCG_Name, "
                          "AVG(2009_CHD_QOF_Value) as 2009_CHD_QOF,"
                          "AVG(2009_CHD_QOF_Upper) as 2009_CHD_QOF_Upper,"
                          "AVG(2009_CHD_QOF_Lower) as 2009_CHD_QOF_Lower,"
                          "AVG(2010_CHD_QOF_Value) as 2010_CHD_QOF,"
                          "AVG(2010_CHD_QOF_Upper) as 2010_CHD_QOF_Upper,"
                          "AVG(2010_CHD_QOF_Lower) as 2010_CHD_QOF_Lower,"
                          "AVG(2011_CHD_QOF_Value) as 2011_CHD_QOF,"
                          "AVG(2011_CHD_QOF_Upper) as 2011_CHD_QOF_Upper,"
                          "AVG(2011_CHD_QOF_Lower) as 2011_CHD_QOF_Lower,"
                          "AVG(2012_CHD_QOF_Value) as 2012_CHD_QOF,"
                          "AVG(2012_CHD_QOF_Upper) as 2012_CHD_QOF_Upper,"
                          "AVG(2012_CHD_QOF_Lower) as 2012_CHD_QOF_Lower, "
                          "AVG(2013_CHD_QOF_Value) as 2013_CHD_QOF,"
                          "AVG(2013_CHD_QOF_Upper) as 2013_CHD_QOF_Upper,"
                          "AVG(2013_CHD_QOF_Lower) as 2013_CHD_QOF_Lower "
                          "FROM TBL_PRACTICE_DATA "
                          "where Practice_Code = %s;",(ccg))
    return data, 200, {'Access-Control-Allow-Origin': '*'}