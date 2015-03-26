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




TODOS = {
    'todo1': {'task': 'build an API'},
    'todo2': {'task': '?????'},
    'todo3': {'task': 'profit!'},
}


def abort_if_todo_doesnt_exist(todo_id):
  if todo_id not in TODOS:
    abort(404, message="Todo {} doesn't exist".format(todo_id))

parser = reqparse.RequestParser()
parser.add_argument('task', type=str)


@swagger.model
class TodoItem:
  """This is an example of a model class that has parameters in its constructor
  and the fields in the swagger spec are derived from the parameters
  to __init__.
  In this case we would have args, arg2 as required parameters and arg3 as
  optional parameter."""
  def __init__(self, arg1, arg2, arg3='123'):
    pass

class Todo(Resource):
  "My TODO API"
  @swagger.operation(
      notes='get a todo item by ID',
      nickname='get',
      # Parameters can be automatically extracted from URLs (e.g. <string:id>)
      # but you could also override them here, or add other parameters.
      parameters=[
          {
            "name": "todo_id_x",
            "description": "The ID of the TODO item",
            "required": True,
            "allowMultiple": False,
            "dataType": 'string',
            "paramType": "path"
          },
          {
            "name": "a_bool",
            "description": "The ID of the TODO item",
            "required": True,
            "allowMultiple": False,
            "dataType": 'boolean',
            "paramType": "path"
          }
      ])
  def get(self, todo_id):
    # This goes into the summary
    """Get a todo task
    This will be added to the <strong>Implementation Notes</strong>.
    It lets you put very long text in your api.
    Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod
    tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim
    veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea
    commodo consequat. Duis aute irure dolor in reprehenderit in voluptate
    velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat
    cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id
    est laborum.
    """
    abort_if_todo_doesnt_exist(todo_id)
    return TODOS[todo_id], 200, {'Access-Control-Allow-Origin': '*'}

  @swagger.operation(
      notes='delete a todo item by ID',
  )
  def delete(self, todo_id):
    abort_if_todo_doesnt_exist(todo_id)
    del TODOS[todo_id]
    return '', 204, {'Access-Control-Allow-Origin': '*'}

  @swagger.operation(
      notes='edit a todo item by ID',
  )
  def put(self, todo_id):
    args = parser.parse_args()
    task = {'task': args['task']}
    TODOS[todo_id] = task
    return task, 201, {'Access-Control-Allow-Origin': '*'}

  def options (self, **args):
    # since this method is not decorated with @swagger.operation it does not
    # get added to the swagger docs
    return {'Allow' : 'GET,PUT,POST,DELETE' }, 200, \
    { 'Access-Control-Allow-Origin': '*', \
      'Access-Control-Allow-Methods': 'GET,PUT,POST,DELETE', \
      'Access-Control-Allow-Headers': 'Content-Type' }



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
    app.run()