from flask import Flask, jsonify
from flask import request
from flaskext.mysql import MySQL

mysql = MySQL()

app = Flask(__name__)

app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'mallard'
app.config['MYSQL_DATABASE_DB'] = 'wePredict'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

@app.route("/Authenticate")
def Authenticate():
    username = request.args.get('UserName')
    password = request.args.get('Password')
    cursor = mysql.connect().cursor()
    cursor.execute("SELECT * from users where username='" + username + "' and password='" + password + "'")
    data = cursor.fetchone()
    if data is None:
        return "Username or Password is wrong"
    else:
        return "Logged in successfully"


@app.route("/COPD")
def COPD():
    return jsonify({'data': 'hi'}), 201

@app.route("/")
def hello():
    return "Hello, apache!!!!!"

if __name__ == "__main__":
    app.debug = True
    app.run()

