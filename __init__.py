from flask import Flask, jsonify
from flask import request
import MySQLdb

app = Flask(__name__)
db = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="mallard", db="wePredict")

@app.route('/testdb')
def testdb():
    cursor = db.cursor()
    cursor.execute("SELECT * from ADRESS");
    return jsonify(data = cursor.fetchall())


@app.route('/getAdress')
def getAdress():
    limit = request.args.get('limit')
    if limit is None:
        cursor = db.cursor()
        cursor.execute("SELECT * from ADRESS");
        return jsonify(data = cursor.fetchall())
    else:
        cursor = db.cursor()
        cursor.execute("SELECT * from ADRESS LIMIT "+limit);
        return jsonify(data = cursor.fetchall())




@app.route('/getSMOKING')
def getSMOKING():
    limit = request.args.get('limit')
    if limit is None:
        cursor = db.cursor()
        cursor.execute("SELECT * from SMOKING");
        return jsonify(data = cursor.fetchall())
    else:
        cursor = db.cursor()
        cursor.execute("SELECT * from SMOKING LIMIT "+limit);
        return jsonify(data = cursor.fetchall())




@app.route('/getPOLLUTION')
def getPOLLUTION():
    limit = request.args.get('limit')
    if limit is None:
        cursor = db.cursor()
        cursor.execute("SELECT * from POLLUTION");
        return jsonify(data = cursor.fetchall())
    else:
        cursor = db.cursor()
        cursor.execute("SELECT * from POLLUTION LIMIT "+limit);
        return jsonify(data = cursor.fetchall())




@app.route('/getFLU')
def getFLU():
    limit = request.args.get('limit')
    if limit is None:
        cursor = db.cursor()
        cursor.execute("SELECT * from FLU");
        return jsonify(data = cursor.fetchall())
    else:
        cursor = db.cursor()
        cursor.execute("SELECT * from FLU LIMIT "+limit);
        return jsonify(data = cursor.fetchall())


@app.route('/getCOPD')
def getCOPD():
    limit = request.args.get('limit')
    if limit is None:
        cursor = db.cursor()
        cursor.execute("SELECT * from COPD");
        return jsonify(data = cursor.fetchall())
    else:
        cursor = db.cursor()
        cursor.execute("SELECT * from COPD LIMIT "+limit);
        return jsonify(data = cursor.fetchall())


@app.route('/getASTHMA_QOF')
def getASTHMA_QOF():
    limit = request.args.get('limit')
    if limit is None:
        cursor = db.cursor()
        cursor.execute("SELECT * from ASTHMA_QOF");
        return jsonify(data = cursor.fetchall())
    else:
        cursor = db.cursor()
        cursor.execute("SELECT * from ASTHMA_QOF LIMIT "+limit);
        return jsonify(data = cursor.fetchall())



@app.route("/")
def hello():
    return "Hello, apache!!!!!"

if __name__ == "__main__":
    app.debug = True
    app.run()

