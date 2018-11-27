from flask import Flask, jsonify, request
from api.recordmodel import Record
from datetime import datetime
app = Flask(__name__)

records = []

@app.route('/api/v1/records', methods=['POST'])
def create_record():
    """ Creates a new record"""
    data = request.get_json()
    record_id = len(records)+1
    created_on = datetime.now()
    record = Record(record_id, data['title'], data['description'], data['status'], data['comments'], created_on, data['location'], data['record_type'], data['images'], data['videos'], data['created_by'])
    records.append(record)
    return jsonify({"message":" Successfully created"}), 201

@app.route('/api/v1/records', methods = ['GET'])
def fetch_record():
    #fetches all user's records
    Records = [record.get_record() for record in records]
    return jsonify({"records": Records})

@app.route('/api/v1/records/<int:record_id>', methods = ['GET'])
def fetch_single_record(record_id):
    fetched_record = []
    record= records[record_id - 1]
    fetched_record.append(record.get_record())
    return jsonify({"record": fetched_record}),200

@app.route('/api/v1/records/<int:record_id>', methods=['PUT'])
def edit_record(record_id):
    # this class enables user modified their records before admin changes its status
    if record_id == 0 or record_id > len(records):
        return jsonify({"message": "Index is out of range"}), 400
    data = request.get_json()
    for record in records:
        if int(record.record_id) == int(record_id):
              record.record_type= data['record_type']
              record.title = data['title']
              record.description = data['description']
              record.location = data['location']
              record.status = data['status']
              record.images = data['images']
              record.videos = data['videos']
              record.created_by = data['created_by']          
    return jsonify({'message': "successfully edited"}), 200

@app.route('/api/v1/records/<int:record_id>', methods=['DELETE'])
def delete_record(record_id):
    # this function enables user delete a record 
    if record_id == 0 or record_id > len(records):
        return jsonify({"message": "Index out of range"}), 400
    for record in records:
        if record.record_id == record_id:
            records.remove(record)
    return jsonify({"message": "record successfully deleted"}), 200




   
    
