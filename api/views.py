from flask import Flask, jsonify, request
from api.models import Record
from datetime import datetime
app = Flask(__name__)

records = []

@app.route('/api/v1/records', methods=['POST'])
def create_record():
    """ Creates a new record"""
    data = request.get_json()
    record_id = len(records)+1
    created_on = datetime.now()
    record = Record(record_id, data['title'], data['description'],data['status'] ,data['comments'], created_on, data['location'], data['record_type'], data['images'], data['videos'], data['created_by'])
    records.append(record)
    return jsonify({"message":" Successfully created"}), 201

@app.route('/api/v1/records', methods = ['GET'])
def fetch_record():
    Records = [record.get_record() for record in records]
    return jsonify({"records": Records})


    
