__author__ = 'robert'

## @package wePredictAPI.api.ccg
#  API Classes that are specific to get CCG Data from the database


from flask import Flask ,g
from flask_cors import CORS
from wePredictAPI.database.db import DB
from flask import Flask, redirect
from flask.ext.restful import reqparse, abort, Api, Resource, fields, marshal_with
from flask_restful_swagger import swagger
import simplejson
import urllib

class CcgList(Resource):
  """
    API Class that define the methods to get list of CCG form the database
  """
  @swagger.operation(
      notes='Get list of all CCG in England',
      nickname='get',
    )
  def get(self):
    """Get list of all CCG in England
    """
    data = g.db.getResult("SELECT Practice_Code,CCG_Name FROM TBL_PRACTICE_INFO group by CCG_Name order by Practice_Code ;")
    return data, 200, {'Access-Control-Allow-Origin': '*'}



class HeatMap(Resource):
  """
    API Class that define the methods to get Heat map data form the database
  """
  @swagger.operation(
      notes='Get Heatmap data',
      nickname='get',
    )
  def get(self):
    """
    Defines what a http get will output for this API route

    :return JSON Opject that cotains all infomtion form the database:
    """
    data = g.db.getResult("SELECT CCG_Name, "

                          "AVG(2009_COPD_QOF_Value) as 2009_COPD, "
                          "AVG(2010_COPD_QOF_Value) as 2010_COPD,"
                          "AVG(2011_COPD_QOF_Value) as 2011_COPD,"
                          "AVG(2012_COPD_QOF_Value) as 2012_COPD,"


                          "AVG(2009_Asthma_Value) as 2009_ASTHMA,"
                          "AVG(2010_Asthma_Value) as 2010_ASTHMA,"
                          "AVG(2011_Asthma_Value) as 2011_ASTHMA, "
                          "AVG(2012_Asthma_Value) as 2012_ASTHMA, "

                          "AVG(2009_Obesity_QOF_Value) as 2009_Obesity_QOF,"
                          "AVG(2010_Obesity_QOF_Value) as 2010_Obesity_QOF,"
                          "AVG(2011_Obesity_QOF_Value) as 2011_Obesity_QOF,"
                          "AVG(2012_Obesity_QOF_Value) as 2012_Obesity_QOF,"

                          "AVG(2009_CHD_QOF_Value) as 2009_CHD_QOF,"
                          "AVG(2010_CHD_QOF_Value) as 2010_CHD_QOF,"
                          "AVG(2011_CHD_QOF_Value) as 2011_CHD_QOF,"
                          "AVG(2012_CHD_QOF_Value) as 2012_CHD_QOF "
                          "FROM TBL_PRACTICE_DATA "
                          "join TBL_PRACTICE_INFO on TBL_PRACTICE_DATA.Practice_Code = TBL_PRACTICE_INFO.Practice_Code "
                          "group by CCG_Name;")
    return data, 200, {'Access-Control-Allow-Origin': '*'}

class CCG_Asmatha_ALL(Resource):
  """
    API Class that define the methods to get Asmatha data for all CCG
  """
  @swagger.operation(
      notes='Get Heatmap data',
      nickname='get',
    )
  def get(self):
    """
    Defines what a http get will output for this API route

    :return data: JSON encoded Object that contains all information form the database
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
  """
    API Class that define the methods to get Asmatha data for certain  CCG
  """
  @swagger.operation(
      notes='Get Heatmap data',
      nickname='get',
    )
  def get(self,ccg_id):
    """
    Defines what a http get will output for this API route
    :param ccg_id: String contain the specific CCG to search for data
    :return data: JSON encoded Object that contains all information form the database
    """

    ccg = urllib.unquote(ccg_id)
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
                          "group by CCG_NAME;",(ccg_id))
    return data, 200, {'Access-Control-Allow-Origin': '*'}

class CCG_COPD_QOF_ALL(Resource):
  """
    API Class that define the methods to get COPD data for all CCG
  """
  @swagger.operation(
      notes='Get Heatmap data',
      nickname='get',
    )
  def get(self):
    """
        Defines what a http get will output for this API route

        :return data: JSON encoded Object that contains all information form the database
    """
    data = g.db.getResult("SELECT CCG_Name, "
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
                          "FROM TBL_PRACTICE_INFO "
                          "join TBL_PRACTICE_DATA on TBL_PRACTICE_INFO.Practice_Code = TBL_PRACTICE_DATA.Practice_Code "
                          "group by CCG_Name;")
    return data, 200, {'Access-Control-Allow-Origin': '*'}

class CCG_COPD_QOF(Resource):
  """
    API Class that define the methods to get COPD data for Certain CCG
  """
  @swagger.operation(
      notes='Get Heatmap data',
      nickname='get',
    )
  def get(self,ccg_id):
    """
        Defines what a http get will output for this API route
        :param ccg_id: String contain the specific CCG to search for data
        :return data: JSON encoded Object that contains all information form the database
    """
    ccg = urllib.unquote(ccg_id)
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
                          "FROM TBL_PRACTICE_INFO "
                          "join TBL_PRACTICE_DATA on "
                          "TBL_PRACTICE_INFO.Practice_Code = TBL_PRACTICE_DATA.Practice_Code "
                          "where CCG_NAME = %s "
                          "group by CCG_NAME;",(ccg_id))
    return data, 200, {'Access-Control-Allow-Origin': '*'}


class CCG_Obesity_QOF_ALL(Resource):
  """
    API Class that define the methods to get Obesity data for all CCG
  """
  @swagger.operation(
      notes='Get Heatmap data',
      nickname='get',
    )
  def get(self):
    """
        Defines what a http get will output for this API route

        :return data: JSON encoded Object that contains all information form the database
    """
    data = g.db.getResult("SELECT CCG_Name, "
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
                          "FROM TBL_PRACTICE_INFO "
                          "join TBL_PRACTICE_DATA on TBL_PRACTICE_INFO.Practice_Code = TBL_PRACTICE_DATA.Practice_Code "
                          "group by CCG_Name;")
    return data, 200, {'Access-Control-Allow-Origin': '*'}

class CCG_Obesity_QOF(Resource):
  """
    API Class that define the methods to get Obesity data for certain CCG
  """
  @swagger.operation(
      notes='Get Heatmap data',
      nickname='get',
    )
  def get(self,ccg_id):
    """
        Defines what a http get will output for this API route
        :param ccg_id: String contain the specific CCG to search for data
        :return data: JSON encoded Object that contains all information form the database
    """
    ccg = urllib.unquote(ccg_id)
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
                          "FROM TBL_PRACTICE_INFO "
                          "join TBL_PRACTICE_DATA on "
                          "TBL_PRACTICE_INFO.Practice_Code = TBL_PRACTICE_DATA.Practice_Code "
                          "where CCG_NAME = %s "
                          "group by CCG_NAME;",(ccg_id))
    return data, 200, {'Access-Control-Allow-Origin': '*'}


class CCG_CHD_QOF_ALL(Resource):
  """
    API Class that define the methods to get CHD data for all CCG
  """
  @swagger.operation(
      notes='Get Heatmap data',
      nickname='get',
    )
  def get(self):
    """
        Defines what a http get will output for this API route
        :return data: JSON encoded Object that contains all information form the database
    """
    data = g.db.getResult("SELECT CCG_Name, "
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
                          "FROM TBL_PRACTICE_INFO "
                          "join TBL_PRACTICE_DATA on TBL_PRACTICE_INFO.Practice_Code = TBL_PRACTICE_DATA.Practice_Code "
                          "group by CCG_Name;")
    return data, 200, {'Access-Control-Allow-Origin': '*'}
class CCG_CHD_QOF(Resource):
  """
    API Class that define the methods to get CHD data for certain CCG
  """
  @swagger.operation(
      notes='Get Heatmap data',
      nickname='get',
    )
  def get(self,ccg_id):
    """
        Defines what a http get will output for this API route
        :param ccg_id: String contain the specific CCG to search for data
        :return data: JSON encoded Object that contains all information form the database
    """
    ccg = urllib.unquote(ccg_id)
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
                          "FROM TBL_PRACTICE_INFO "
                          "join TBL_PRACTICE_DATA on "
                          "TBL_PRACTICE_INFO.Practice_Code = TBL_PRACTICE_DATA.Practice_Code "
                          "where CCG_NAME = %s "
                          "group by CCG_NAME;",(ccg_id))
    return data, 200, {'Access-Control-Allow-Origin': '*'}



class CCG_COPD_Admissions_ALL(Resource):
  """
    API Class that define the methods to get COPD_Admissions data for all CCG
  """
  @swagger.operation(
      notes='Get Heatmap data',
      nickname='get',
    )
  def get(self):
    """
        Defines what a http get will output for this API route
        :return data: JSON encoded Object that contains all information form the database
    """
    data = g.db.getResult("SELECT CCG_Name, "
                          "AVG(2010_COPD_Admissions) as 2010_COPD_Admissions,"
                          "AVG(2010_COPD_Admissions_Lower) as 2010_COPD_Admissions_Lower,"
                          "AVG(2010_COPD_Admissions_Upper) as 2010_COPD_Admissions_Upper,"
                          "AVG(2011_COPD_Admissions) as 2011_COPD_Admissions,"
                          "AVG(2011_COPD_Admissions_Lower) as 2011_COPD_Admissions_Lower,"
                          "AVG(2011_COPD_Admissions_Upper) as 2011_COPD_Admissions_Upper,"
                          "AVG(2012_COPD_Admissions) as 2012_COPD_Admissions,"
                          "AVG(2012_COPD_Admissions_Lower) as 2012_COPD_Admissions_Lower,"
                          "AVG(2012_COPD_Admissions_Upper) as 2012_COPD_Admissions_Upper "
                          "FROM TBL_PRACTICE_INFO "
                          "join TBL_PRACTICE_DATA on TBL_PRACTICE_INFO.Practice_Code = TBL_PRACTICE_DATA.Practice_Code "
                          "group by CCG_Name;")
    return data, 200, {'Access-Control-Allow-Origin': '*'}
class CCG_COPD_Admissions(Resource):
  """
    API Class that define the methods to get COPD_Admissions data for certain CCG
  """
  @swagger.operation(
      notes='Get Heatmap data',
      nickname='get',
    )
  def get(self,ccg_id):
    """
        Defines what a http get will output for this API route
        :param ccg_id: String contain the specific CCG to search for data
        :return data: JSON encoded Object that contains all information form the database
    """
    ccg = urllib.unquote(ccg_id)
    data = g.db.getResultParamaters("SELECT CCG_Name, "
                          "AVG(2010_COPD_Admissions) as 2010_COPD_Admissions,"
                          "AVG(2010_COPD_Admissions_Lower) as 2010_COPD_Admissions_Lower,"
                          "AVG(2010_COPD_Admissions_Upper) as 2010_COPD_Admissions_Upper,"
                          "AVG(2011_COPD_Admissions) as 2011_COPD_Admissions,"
                          "AVG(2011_COPD_Admissions_Lower) as 2011_COPD_Admissions_Lower,"
                          "AVG(2011_COPD_Admissions_Upper) as 2011_COPD_Admissions_Upper,"
                          "AVG(2012_COPD_Admissions) as 2012_COPD_Admissions,"
                          "AVG(2012_COPD_Admissions_Lower) as 2012_COPD_Admissions_Lower,"
                          "AVG(2012_COPD_Admissions_Upper) as 2012_COPD_Admissions_Upper "
                          "FROM TBL_PRACTICE_INFO "
                          "join TBL_PRACTICE_DATA on TBL_PRACTICE_INFO.Practice_Code = TBL_PRACTICE_DATA.Practice_Code "
                          "where CCG_NAME = %s "
                          "group by CCG_NAME;",(ccg_id))
    return data, 200, {'Access-Control-Allow-Origin': '*'}


class CCG_Smoking_ALL(Resource):
  """
    API Class that define the methods to get smoking prevalence data for all CCG
  """
  @swagger.operation(
      notes='Get Heatmap data',
      nickname='get',
    )
  def get(self):
    """
        Defines what a http get will output for this API route
        :return data: JSON encoded Object that contains all information form the database
    """
    data = g.db.getResult("SELECT CCG_Name, "
						  "AVG(2012_smoking_prevalence_Value) as 2012_smoking_prevalence,"
                          "AVG(2012_smoking_prevalence_Upper) as 2012_smoking_prevalence_Upper,"
                          "AVG(2012_smoking_prevalence_Lower) as 2012_smoking_prevalence_Lower,"
                          "AVG(2013_smoking_prevalence_Value) as 2013_smoking_prevalence,"
                          "AVG(2013_smoking_prevalence_Upper) as 2013_smoking_prevalence_Upper,"
                          "AVG(2013_smoking_prevalence_Lower) as 2013_smoking_prevalence_Lower "
                          "FROM TBL_PRACTICE_INFO "
                          "join TBL_PRACTICE_DATA on TBL_PRACTICE_INFO.Practice_Code = TBL_PRACTICE_DATA.Practice_Code "
                          "group by CCG_Name;")
    return data, 200, {'Access-Control-Allow-Origin': '*'}
class CCG_Smoking(Resource):
  """
    API Class that define the methods to get smoking prevalence data for certain CCG
  """
  @swagger.operation(
      notes='Get Heatmap data',
      nickname='get',
    )
  def get(self,ccg_id):
    """
        Defines what a http get will output for this API route
        :param ccg_id: String contain the specific CCG to search for data
        :return data: JSON encoded Object that contains all information form the database
    """
    ccg = urllib.unquote(ccg_id)
    data = g.db.getResultParamaters("SELECT CCG_Name, "
						  "AVG(2012_smoking_prevalence_Value) as 2012_smoking_prevalence,"
                          "AVG(2012_smoking_prevalence_Upper) as 2012_smoking_prevalence_Upper,"
                          "AVG(2012_smoking_prevalence_Lower) as 2012_smoking_prevalence_Lower,"
                          "AVG(2013_smoking_prevalence_Value) as 2013_smoking_prevalence,"
                          "AVG(2013_smoking_prevalence_Upper) as 2013_smoking_prevalence_Upper,"
                          "AVG(2013_smoking_prevalence_Lower) as 2013_smoking_prevalence_Lower "
                          "FROM TBL_PRACTICE_INFO "
                          "join TBL_PRACTICE_DATA on TBL_PRACTICE_INFO.Practice_Code = TBL_PRACTICE_DATA.Practice_Code "
                          "where CCG_NAME = %s "
                          "group by CCG_NAME;",(ccg_id))
    return data, 200, {'Access-Control-Allow-Origin': '*'}


class CCG_Flu_ALL(Resource):
  """
    API Class that define the methods to get Flu prevalence data for all CCG
  """
  @swagger.operation(
      notes='Get Heatmap data',
      nickname='get',
    )
  def get(self):
    """
        Defines what a http get will output for this API route
        :return data: JSON encoded Object that contains all information form the database
    """
    data = g.db.getResult("SELECT CCG_Name, "
                                    "AVG(2010_flu_vaccine_65_Value) as 2010_flu65,"
                                    "AVG(2010_flu_vaccine_66_Lower) as 2010_flu65_Upper,"
                                    "AVG(2010_flu_vaccine_67_Upper) as 2010_flu65_Lower,"
                                    "AVG(2010_flu_vaccine_06_Value) as 2010_flu06,"
                                    "AVG(2010_flu_vaccine_07_Lower) as 2010_flu06_Lower,"
                                    "AVG(2010_flu_vaccine_08_Upper) as 2010_flu06_Upper "
                          "FROM TBL_PRACTICE_INFO "
                          "join TBL_PRACTICE_DATA on TBL_PRACTICE_INFO.Practice_Code = TBL_PRACTICE_DATA.Practice_Code "
                          "group by CCG_Name;")
    return data, 200, {'Access-Control-Allow-Origin': '*'}
class CCG_Flu(Resource):
  """
    API Class that define the methods to get Flu data for certain CCG
  """
  @swagger.operation(
      notes='Get Heatmap data',
      nickname='get',
    )
  def get(self,ccg_id):
    """
        Defines what a http get will output for this API route
        :param ccg_id: String contain the specific CCG to search for data
        :return data: JSON encoded Object that contains all information form the database
    """
    ccg = urllib.unquote(ccg_id)
    data = g.db.getResultParamaters("SELECT CCG_Name, "
                                    "AVG(2010_flu_vaccine_65_Value) as 2010_flu65,"
                                    "AVG(2010_flu_vaccine_66_Lower) as 2010_flu65_Upper,"
                                    "AVG(2010_flu_vaccine_67_Upper) as 2010_flu65_Lower,"
                                    "AVG(2010_flu_vaccine_06_Value) as 2010_flu06,"
                                    "AVG(2010_flu_vaccine_07_Lower) as 2010_flu06_Lower,"
                                    "AVG(2010_flu_vaccine_08_Upper) as 2010_flu06_Upper "
                          "FROM TBL_PRACTICE_INFO "
                          "join TBL_PRACTICE_DATA on TBL_PRACTICE_INFO.Practice_Code = TBL_PRACTICE_DATA.Practice_Code "
                          "where CCG_NAME = %s "
                          "group by CCG_NAME;",(ccg_id))
    return data, 200, {'Access-Control-Allow-Origin': '*'}

