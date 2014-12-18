from flask import Flask, jsonify
from flask import request
import MySQLdb

app = Flask(__name__)
db = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="mallard", db="wePredict")

@app.route('/testdb')
def testdb():
    cursor = db.cursor()
    cursor.execute("SELECT * from ADRESS LIMIT 5");
    return jsonify(data = cursor.fetchall())

@app.route("/")
def hello():
    return "Hello, apache!!!!!"

if __name__ == "__main__":
    app.debug = True
    app.run()

