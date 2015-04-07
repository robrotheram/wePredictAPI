
## @package wePredictAPI.app
#  Starts up the Server and contains the loading the API routes


from flask import g
from flask_cors import CORS
from wePredictAPI.database.db import DB
from flask import Flask, redirect
from flask.ext.restful import reqparse, Api, Resource
from flask_restful_swagger import swagger
from api.ccg import *
from api.practice import *


"""
\mainpage WePredict API

 \section intro_sec Introduction

This project is the backend API to the WePredict Health Visualisation. This Document contains specific information for
what every file and function does. For API documentation for use of the data can be found here:
<a href="http://wepredict.robrotheram.com/docs">http://wepredict.robrotheram.com/docs</a>
 <br>
 Project Authors
 <ul>
 <li>Robert Fletcher</li>
 </ul>

 \section install_sec Simple Installation

 \subsection step1 Step 1: Create a account in Openshift:
 <a href="https://www.openshift.com/">https://www.openshift.com/</a>
 \subsection step2 Step 2: Add a application: Go to the python and click show all and select the Flask container
 \subsection step3 Step 5: Choose an name for the container
 \subsection step4 Step 4: Change the Source Code to https://github.com/robrotheram/wePredictAPI.git
 \subsection step5 Step 5: Add Application
 \subsection step6 Step 6: Add a MySQL Database to the container
 \subsection step7 Step 7: Log into the application database using a application similar to Mysql Workbench.
 To connect the the database using this tutorial
 <a href="https://forums.openshift.com/connecting-to-openshift-mysql-using-workbench">
 https://forums.openshift.com/connecting-to-openshift-mysql-using-workbench</a>

 \subsection step8 Step 8: import the database form the dump data.
 \subsection step9 Step 9: Application should now work



"""

## Setup A Flask App
app = Flask(__name__)
## Enable Cross-origin resource sharing so that the API and front end can be on different servers
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['PROPAGATE_EXCEPTIONS'] = True

##API Setup using the swagger Lib for Auto documenting
api = swagger.docs(Api(app), apiVersion='0.1',
                   basePath='http://wepredict.robrotheram.com',
                   resourcePath='/',
                   produces=["application/json", "text/html"],
                   api_spec_url='/api/spec',
                   description='WePredict API')


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

api.add_resource(CCG_COPD_Admissions_ALL, '/ccg/COPDAdmissions')
api.add_resource(CCG_COPD_Admissions, '/ccg/COPDAdmissions/<string:ccg_id>')

api.add_resource(CCG_Smoking_ALL, '/ccg/smoking')
api.add_resource(CCG_Smoking, '/ccg/smoking/<string:ccg_id>')

api.add_resource(CCG_Flu_ALL, '/ccg/flu')
api.add_resource(CCG_Flu, '/ccg/flu/<string:ccg_id>')





api.add_resource(HeatMap, '/ccg/heat_map')
api.add_resource(PracticeData, '/practice/data/<string:practice_id>')



api.add_resource(Practice, '/practice/<string:ccg_id>')
api.add_resource(PracticeList, '/practice')


api.add_resource(Practice_Asmatha, '/practice/asmatha/<string:practice_id>')

api.add_resource(Practice_CHD_QOF, '/practice/chd/<string:practice_id>')

api.add_resource(Practice_COPD_QOF, '/practice/copd/<string:practice_id>')

api.add_resource(Practice_Obesity_QOF, '/practice/obesity/<string:practice_id>')



@app.route('/docs')
def docs():
    """
    URL route to the API Documentation
    @retval       Url Path
    """
    return redirect('/static/docs/index.html')

@app.route('/')
def homepage():
    """
    URL route to the frontend of the application
    @retval       Url Path
    """
    return redirect('/static/front/app/index.html')



@app.before_request
def before_request():
    """
    Sets Up the Database connection pool into the Flask Global variables g that then can be used across the other modules

    """
    g.db = DB()

if __name__ == '__main__':
    app.run(debug=True)