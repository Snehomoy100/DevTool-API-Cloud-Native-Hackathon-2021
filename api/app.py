from flask import Flask, json, jsonify, request # request module imported  
from flask_sqlalchemy import SQLAlchemy # using SQLite db for our database operations
import sqlite3 # sqlite3 database as the database 
import yaml 
from yaml import load, dump
from yaml.loader import SafeLoader
from kubernetes import client, config, watch

from datetime import datetime # for the timestamp things of our db operation

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app) # database object

# creating an API object
# api = Api(app)

sqliteConnection = sqlite3.connect('test.db') # database connection
cursor = sqliteConnection.cursor()
print("Database created and Successfully Connected to SQLite")





# Configs can be set in Configuration class directly or using helper utility
config.load_kube_config()

v1 = client.CoreV1Api()
count = 10
w = watch.Watch()
for event in w.stream(v1.list_namespace, _request_timeout=60):
    print("Event: %s %s" % (event['type'], event['object'].metadata.name))
    count -= 1
    if not count:
        w.stop()

print("Ended.")








with open('fail.yml') as f:
    json_data = yaml.load(f, Loader=SafeLoader)


@app.route('/')
def health_check():
  return 'Test Connection'

# search api
@app.route("/search", methods=["POST"])
def grafana_search():
    targets = find_targets()
    return json.dumps(targets)

# query api

@app.route('/query', methods=['POST'])
def query():
    req = request.get_json()
    data = json_data
    return jsonify(data)


if __name__ == "__main__": # running the app
    app.run(debug=True)