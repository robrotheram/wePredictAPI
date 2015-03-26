from flask import Flask ,g
from flask_cors import CORS
from wePredictAPI.database.db import DB
from flask import Flask, redirect
from flask.ext.restful import reqparse, abort, Api, Resource, fields,\
    marshal_with
from flask_restful_swagger import swagger


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

class Ccg():
    def get(self):
        data = g.db.getResult("SELECT CCG FROM CCG GROUP BY CCG")
        js_data = []
        for obj in data:
            objjst = {"CCG": obj['CCG']}
            js_data.append(objjst)
        return js_data, 200, {'Access-Control-Allow-Origin': '*'}


api.add_resource(Ccg, '/ccg')

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