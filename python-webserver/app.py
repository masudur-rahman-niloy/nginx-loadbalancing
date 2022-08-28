from flask import Flask, jsonify
import os
import pymysql.cursors

app = Flask(__name__)

MYSQL_HOST = os.getenv('MYSQL_HOST')
MYSQL_USER = os.getenv('MYSQL_USER')
MYSQL_PASS = os.getenv('MYSQL_PASS')
MYSQL_DBN = os.getenv('MYSQL_DBN')
MYSQL_PORT = os.getenv('MYSQL_PORT', '3306')

def check_connection():
    try:
        connection = pymysql.connect(
                    host=MYSQL_HOST,
                    user=MYSQL_USER,
                    password=MYSQL_PASS,
                    db=MYSQL_DBN,
                    port=int(MYSQL_PORT),
                    cursorclass=pymysql.cursors.DictCursor
            )
        return f"Connection successful"
    except Exception as e:
        return f"Connection failure: {str(e)}"
    

@app.route("/")
def index():
    return "Hello, this is index"

@app.route("/connection")
def connection():
    res = check_connection()
    return res

if __name__ == '__main__':
    app.run(host="0.0.0.0", port="3000")