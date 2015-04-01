from flask import g
from flask_cors import CORS
from wePredictAPI.database.db import DB
from flask import Flask, redirect
from flask.ext.restful import reqparse, Api, Resource
from flask_restful_swagger import swagger
from api.ccg import CcgList, HeatMap,CCG_Asmatha,CCG_Asmatha_ALL, CCG_CHD_QOF,CCG_CHD_QOF_ALL,CCG_COPD_QOF,CCG_COPD_QOF_ALL,CCG_Obesity_QOF,CCG_Obesity_QOF_ALL
from api.practice import PracticeData, Practice, PracticeList, Practice_Asmatha,Practice_CHD_QOF,Practice_COPD_QOF,Practice_Obesity_QOF


"""
@package app
Compute the first ten numbers in the Fibonacci sequence
"""

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['PROPAGATE_EXCEPTIONS'] = True




class error(Resource):
  "My TODO API"
  @swagger.operation(
      notes='Get list of all CCG in England',
      nickname='get',
    )
  def get(self):
    """
    Return a Fibonacci number

    @param    n   Number in the sequence to return
    @retval       The nth Fibonacci number
    """
    data = g.db.getResult("SELECT Practice_Code,CCG_Name FROM TBL_PRACTICE_INFO group by CCG_Name;")
    return data, 200, {'Access-Control-Allow-Origin': '*'}




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






api.add_resource(CcgList, '/ccg')

api.add_resource(CCG_Asmatha_ALL, '/ccg/asmatha')
api.add_resource(CCG_Asmatha, '/ccg/asmatha/<string:ccg_id>')

api.add_resource(CCG_CHD_QOF_ALL, '/ccg/chd')
api.add_resource(CCG_CHD_QOF, '/ccg/chd/<string:ccg_id>')

api.add_resource(CCG_COPD_QOF_ALL, '/ccg/copd')
api.add_resource(CCG_COPD_QOF, '/ccg/copd/<string:ccg_id>')

api.add_resource(CCG_Obesity_QOF_ALL, '/ccg/obesity')
api.add_resource(CCG_Obesity_QOF, '/ccg/obesity/<string:ccg_id>')




api.add_resource(HeatMap, '/ccg/heat_map')
api.add_resource(PracticeData, '/practice/data/<string:practice_id>')
api.add_resource(Practice, '/practice/<string:practice_id>')
api.add_resource(PracticeList, '/practice')


api.add_resource(Practice_Asmatha, '/practice/asmatha/<string:practice_id>')

api.add_resource(Practice_CHD_QOF, '/practice/chd/<string:practice_id>')

api.add_resource(Practice_COPD_QOF, '/practice/copd/<string:practice_id>')

api.add_resource(Practice_Obesity_QOF, '/practice/obesity/<string:practice_id>')



@app.route('/docs')
def docs():
    """
    Return a Fibonacci number

    @param    n   Number in the sequence to return
    @retval       The nth Fibonacci number
    """
    return redirect('/static/docs/index.html')




@app.before_request
def before_request():
    g.db = DB()


#import wePredictAPI.views.v1
#import wePredictAPI.views.v1.Asmtha
#import wePredictAPI.views.v1.COPD
#import wePredictAPI.views.v1.flu
#import wePredictAPI.views.v1.MedicalCenters
#import wePredictAPI.views.v1.Pollution
#import wePredictAPI.views.v1.smoking

if __name__ == '__main__':
    app.run(debug=True)