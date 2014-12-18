from flask import Flask, jsonify
from flask import request
from flask.ext.sqlalchemy import SQLAlchemy
db = SQLAlchemy()
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:mallard@localhost/wePredict'
from models import db
db.init_app(app)

@app.route('/testdb')
def testdb():
  if db.session.query("1").from_statement("SELECT 1").all():
    return 'It works.'
  else:
    return 'Something is broken.'

@app.route("/")
def hello():
    return "Hello, apache!!!!!"

if __name__ == "__main__":
    app.debug = True
    app.run()

