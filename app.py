from flask import Flask,render_template,jsonify

import urllib.request, json

import sqlite3
import controller


def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

app = Flask(__name__)
app.config['SECRET_KEY'] = 'JR@9846673939'
  

#api to fetch all data
@app.route('/api/mtr', methods=["GET"])
def get_data():
    datas = controller.get_data()
    return jsonify(datas)

#view function for index(list all meters) using API
@app.route('/meters/')
def index():
    url = "http://127.0.0.1:5000/api/mtr"
    response = urllib.request.urlopen(url)
    data = response.read()
    lists = json.loads(data)
    return render_template ("index.html", lists=lists)    

#api to fetch one particular data by id
@app.route("/api/mtr/<id>", methods=["GET"])
def get_data_by_id(id):
    data = controller.get_by_id(id)
    return jsonify(data)  

#view function for meter data using API
@app.route('/meters/<id>')
def meter_data(id):
    url = f"http://127.0.0.1:5000/api/mtr/{id}"
    response = urllib.request.urlopen(url)
    data = response.read()
    details = json.loads(data)
    return render_template ("details.html", details=details)        


if __name__ == "__main__":
    app.run(debug=True)    

#view functions without using API
# @app.route('/meters/')
# def index():
#     conn = get_db_connection()
#     lists = conn.execute('SELECT * FROM meters').fetchall()

#     # print(lists)
#     return render_template('index.html', lists=lists)    
   
# @app.route('/meters/meter_data/<int:pk>')
# def meter_data(pk):
#     conn = get_db_connection()
#     details = conn.execute(f"SELECT * FROM meter_data WHERE meter_id = {pk} ").fetchall()
#     return render_template('details.html', details=details)      