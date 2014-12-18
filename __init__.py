from flask import Flask, jsonify
from flask import request
import MySQLdb

app = Flask(__name__)

app.config['DEBUG'] = True
app.config['PROPAGATE_EXCEPTIONS'] = True


host="localhost"
port=3306
port=330
user="root"
passwd="mallard"
dbs="wePredict"


@app.route('/getadress')
def getAdress():
    limit = request.args.get('limit')
    if limit is None:
        db = MySQLdb.connect(host, port, user, passwd, dbs)
        cursor = db.cursor()
        cursor.execute("SELECT * from ADRESS");
        db.close()
        return jsonify(data = cursor.fetchall())
    else:
        db = MySQLdb.connect(host, port, user, passwd, dbs)
        cursor = db.cursor()
        cursor.execute("SELECT * from ADRESS LIMIT "+limit);
        db.close()
        return jsonify(data = cursor.fetchall())

@app.route('/getsmoking')
def getsmoking():
    limit = request.args.get('limit')
    if limit is None:
        db = MySQLdb.connect(host, port, user, passwd, dbs)
        cursor = db.cursor()
        cursor.execute("SELECT * from SMOKING");
        db.close()
        return jsonify(data = cursor.fetchall())
    else:
        db = MySQLdb.connect(host, port, user, passwd, dbs)
        cursor = db.cursor()
        cursor.execute("SELECT * from SMOKING LIMIT "+limit);
        db.close()
        return jsonify(data = cursor.fetchall())

@app.route('/getflu')
def getflu():
    limit = request.args.get('limit')
    if limit is None:
        db = MySQLdb.connect(host, port, user, passwd, dbs)
        cursor = db.cursor()
        cursor.execute("SELECT * from FLU");
        db.close()
        return jsonify(data = cursor.fetchall())
    else:
        db = MySQLdb.connect(host, port, user, passwd, dbs)
        cursor = db.cursor()
        cursor.execute("SELECT * from FLU LIMIT "+limit);
        db.close()
        return jsonify(data = cursor.fetchall())

@app.route('/getcopd')
def getcopd():
    limit = request.args.get('limit')
    if limit is None:
        db = MySQLdb.connect(host, port, user, passwd, dbs)
        cursor = db.cursor()
        cursor.execute("SELECT * from COPD");
        db.close()
        return jsonify(data = cursor.fetchall())
    else:
        db = MySQLdb.connect(host, port, user, passwd, dbs)
        cursor = db.cursor()
        cursor.execute("SELECT * from COPD LIMIT "+limit);
        db.close()
        return jsonify(data = cursor.fetchall())

@app.route('/getasmtha')
def getAsmtha():
    limit = request.args.get('limit')
    if limit is None:
        db = MySQLdb.connect(host, port, user, passwd, dbs)
        cursor = db.cursor()
        cursor.execute("SELECT * from ASTHMA_QOF");
        db.close()
        return jsonify(data = cursor.fetchall())
    else:
        db = MySQLdb.connect(host, port, user, passwd, dbs)
        cursor = db.cursor()
        cursor.execute("SELECT * from ASTHMA_QOF LIMIT "+limit);
        db.close()
        return jsonify(data = cursor.fetchall())

@app.route('/getpollution')
def getPollution():
    limit = request.args.get('limit')
    if limit is None:
        db = MySQLdb.connect(host, port, user, passwd, dbs)
        cursor = db.cursor()
        cursor.execute("SELECT * from POLLUTION");
        db.close()
        return jsonify(data = cursor.fetchall())
    else:
        db = MySQLdb.connect(host, port, user, passwd, dbs)
        cursor = db.cursor()
        cursor.execute("SELECT * from POLLUTION LIMIT "+limit);
        db.close()
        return jsonify(data = cursor.fetchall())


@app.route("/")
def hello():
    return "Hello, apache!!!!!<br/>"