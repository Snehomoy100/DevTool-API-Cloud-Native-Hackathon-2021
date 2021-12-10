from flask import Flask, json, jsonify, request
from flask_sqlalchemy import SQLAlchemy # using SQLite db for our database operations

# have to build the REST API


from datetime import datetime # for the timestamp things of our db operation

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app) # database object

# creating an API object
# api = Api(app)

class Todo(db.Model): # database model
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    completed = db.Column(db.Integer, default=0)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    def __repr__(self):
        return '<Task %r>' % self.id


@app.route('/data', methods = ['GET', 'POST'])
def home():
    if(request.method == 'GET'): # api for GET req 
  
        data = "hello world"
        return jsonify({'data': data}), 200
    

    if(request.method == 'POST'): # api for POST req
        data = request.get_json()
        return jsonify({'data': data}), 201 # status code
    
    # have to integrate the POST with the db


if __name__ == "__main__": # running the app
    app.run(debug=True)