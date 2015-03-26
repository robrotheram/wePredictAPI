from flask import Flask ,g
from flask_cors import CORS
from wePredictAPI.database.db import DB
from flask import Flask, redirect
from flask.ext.restful import reqparse, abort, Api, Resource, fields,\
    marshal_with
from flask_restful_swagger import swagger
import urllib


app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['PROPAGATE_EXCEPTIONS'] = True




###################################
# This is important:
api = swagger.docs(Api(app), apiVersion='0.1',
                   basePath='http://wepredict.robrotheram.com',
                   resourcePath='/',
                   produces=["application/json", "text/html"],
                   api_spec_url='/api/spec',
                   description='WePredict API')
###################################

parser = reqparse.RequestParser()
parser.add_argument('task', type=str)



class CcgList(Resource):
  "My TODO API"
  @swagger.operation(
      notes='Get list of all CCG in England',
      nickname='get',
    )
  def get(self):
    """Get list of all CCG in England
    """
    data = g.db.getResult("SELECT CCG FROM CCG GROUP BY CCG")
    js_data = []
    for obj in data:
        objjst = {"CCG": obj['CCG']}
        js_data.append(objjst)
    return js_data, 200, {'Access-Control-Allow-Origin': '*'}


class PracticeList(Resource):
  "My TODO API"
  @swagger.operation(
      notes='Get list of all Practice in CCG',
      nickname='get',
    )
  def get(self):
    """Get list of all CCG in England
    """
    qurry = ("SELECT Practice_Name FROM ADRESS join CCG on PracticeCode = CCG.Practice_Code ")
    data = g.db.getResult(qurry)
    js_data = []
    for obj in data:
        objjst = {"Practice": obj['Practice_Name']}
        js_data.append(objjst)
    return js_data, 200, {'Access-Control-Allow-Origin': '*'}


class Practice(Resource):
  "My TODO API"
  @swagger.operation(
      notes='Get a Practice in CCG',
      nickname='get',
    )
  def get(self,practice_id):
    """Get list of all CCG in England
    """
    prac = urllib.unquote(practice_id)
    qurry = ("SELECT Practice_Name FROM ADRESS join CCG on PracticeCode = CCG.Practice_Code where CCG = '"+prac+"';")
    data = g.db.getResult(qurry)
    js_data = []
    for obj in data:
        objjst = {"Practice": obj['Practice_Name']}
        js_data.append(objjst)
    return js_data, 200, {'Access-Control-Allow-Origin': '*'}






api.add_resource(CcgList, '/ccg')
api.add_resource(PracticeList, '/practice')
api.add_resource(Practice, '/practice/<string:practice_id>')

@app.route('/docs')
def docs():
  return redirect('/static/docs/index.html')




@app.before_request
def before_request():
    g.db = DB()


import wePredictAPI.views.v1
import wePredictAPI.views.v1.Asmtha
import wePredictAPI.views.v1.COPD
import wePredictAPI.views.v1.flu
import wePredictAPI.views.v1.MedicalCenters
import wePredictAPI.views.v1.Pollution
import wePredictAPI.views.v1.smoking

if __name__ == '__main__':
    app.run(debug=True)