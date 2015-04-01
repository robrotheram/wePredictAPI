__author__ = 'robert'

## @package wePredictAPI.api.practice
#  API Classes that are specific to get Practice Data from the database



from flask import g
from flask.ext.restful import reqparse, abort, Api, Resource, fields, marshal_with
from flask_restful_swagger import swagger
import urllib


class Practice(Resource):
  """
    API Class that define the methods to get List of practices for a certain CCG
  """
  @swagger.operation(
      notes='Get a Practice in CCG',
      nickname='get',
    )
  def get(self,ccg_id):
    """
    Defines what a http get will output for this API route
    :param ccg_id: String contain the specific CCG to search for data
    :return data: JSON encoded Object that contains all information form the database
    """
    prac = urllib.unquote(ccg_id)
    print "practice Data - "+prac
    data = g.db.getResultParamaters("SELECT Practice_Code, Practice_Name  FROM TBL_PRACTICE_INFO where CCG_Name = %s order by Practice_Code ;",(prac))
    return data, 200, {'Access-Control-Allow-Origin': '*'}




class PracticeList(Resource):
  """
    API Class that define the methods to get List of practices for England
  """
  @swagger.operation(
      notes='Get list of all Practice in CCG',
      nickname='get',
    )
  def get(self):
    """
    Defines what a http get will output for this API route

    :return data: JSON encoded Object that contains all information form the database
    """
    data = g.db.getResult("SELECT Practice_Code,Practice_Name FROM TBL_PRACTICE_INFO")
    return data, 200, {'Access-Control-Allow-Origin': '*'}


class PracticeData(Resource):
  """
    API Class that define the methods to get all data for a certain practice
  """
  @swagger.operation(
      notes='Get Data of a specific Practice in CCG',
      nickname='get',
    )
  def get(self,practice_id):
    """
    Defines what a http get will output for this API route
    :param ccg_id: String contain the specific CCG to search for data
    :return data: JSON encoded Object that contains all information form the database
    """
    practice = urllib.unquote(practice_id)
    qurry = ("select * from TBL_PRACTICE_DATA where Practice_Code ='"+practice+"' ")
    data = g.db.getResult(qurry)
    return data, 200, {'Access-Control-Allow-Origin': '*'}



class Practice_Asmatha(Resource):
  """
    API Class that define the methods to get all Asmatha for a certain practice
  """
  @swagger.operation(
      notes='Get Heatmap data',
      nickname='get',
    )
  def get(self,practice_id):
    """
    Defines what a http get will output for this API route
    :param ccg_id: String contain the specific CCG to search for data
    :return data: JSON encoded Object that contains all information form the database
    """
    ccg = urllib.unquote(practice_id)
    data = g.db.getResultParamaters("SELECT Practice_Code, "
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
                          "FROM TBL_PRACTICE_DATA "
                          "where Practice_Code = %s;",(ccg))
    return data, 200, {'Access-Control-Allow-Origin': '*'}

class Practice_COPD_QOF(Resource):
  """
    API Class that define the methods to get all COPD for a certain practice
  """
  @swagger.operation(
      notes='Get Heatmap data',
      nickname='get',
    )
  def get(self,practice_id):
    """
    Defines what a http get will output for this API route
    :param ccg_id: String contain the specific CCG to search for data
    :return data: JSON encoded Object that contains all information form the database
    """
    ccg = urllib.unquote(practice_id)
    data = g.db.getResultParamaters("SELECT Practice_Code, "
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
  """
    API Class that define the methods to get all obesity for a certain practice
  """
  @swagger.operation(
      notes='Get Heatmap data',
      nickname='get',
    )
  def get(self,practice_id):
    """
    Defines what a http get will output for this API route
    :param ccg_id: String contain the specific CCG to search for data
    :return data: JSON encoded Object that contains all information form the database
    """
    ccg = urllib.unquote(practice_id)
    data = g.db.getResultParamaters("SELECT Practice_Code, "
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
  """
    API Class that define the methods to get all CHD for a certain practice
  """
  @swagger.operation(
      notes='Get Heatmap data',
      nickname='get',
    )
  def get(self,practice_id):
    """
    Defines what a http get will output for this API route
    :param ccg_id: String contain the specific CCG to search for data
    :return data: JSON encoded Object that contains all information form the database
    """
    ccg = urllib.unquote(practice_id)
    data = g.db.getResultParamaters("SELECT Practice_Code, "
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