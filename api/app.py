from flask import Flask, json, jsonify, request # request module imported  
from flask_sqlalchemy import SQLAlchemy # using SQLite db for our database operations
import sqlite3 # sqlite3 database as the database 
import yaml 
from yaml import load, dump
from yaml.loader import SafeLoader


from datetime import datetime # for the timestamp things of our db operation

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app) # database object

# creating an API object
# api = Api(app)

sqliteConnection = sqlite3.connect('test.db') # database connection
cursor = sqliteConnection.cursor()
print("Database created and Successfully Connected to SQLite")


@app.route('/')
def health_check():
  return 'Test Connection'

# search api
@app.route('/search', methods=['POST'])
def search():
  return jsonify(['my_series', 'another_series'])

# query api

# @app.route('/query', methods=['POST'])
# def query():
#     req = request.get_json()
#     data = 
#     return jsonify(data)


if __name__ == "__main__": # running the app
    app.run(debug=True)