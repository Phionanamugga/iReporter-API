from flask import Flask, jsonify, request
from api.models import Record, User
from datetime import datetime
app = Flask(__name__)

records = []


@app.route('/api/v1/records', methods=['POST'])
def create_record():
    # Creates a new record
    data = request.get_json()
    record_id = len(records)+1
    created_on = datetime.now()
    record = Record(record_id, data['title'], data['description'],
                    data['status'], data['comments'],
                    created_on, data['location'], data['record_type'],
                    data['images'], data['videos'], data['created_by'])
    records.append(record)
    return jsonify({"message": " Successfully created"}), 201


@app.route('/api/v1/records', methods=['GET'])
def fetch_record():
    # fetches all user's records
    Records = [record.get_record() for record in records]
    return jsonify({"records": Records})


@app.route('/api/v1/records/<int:record_id>', methods=['GET'])
def fetch_single_record(record_id):
    fetched_record = []
    record = records[record_id - 1]
    fetched_record.append(record.get_record())
    return jsonify({"record": fetched_record}), 200


@app.route('/api/v1/records/<int:record_id>', methods=['PUT'])
def edit_record(record_id):
    # function for editing a record
    if record_id == 0 or record_id > len(records):
        return jsonify({"message": "Index is out of range"}), 400
    data = request.get_json()
    for record in records:
        if int(record.record_id) == int(record_id):
            record.record_type = data['record_type']
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
    # this function enables user delete record
    if record_id == 0 or record_id > len(records):
        return jsonify({"message": "Index out of range"}), 400
    for record in records:
        if record.record_id == record_id:
            records.remove(record)
    return jsonify({"message": "record successfully deleted"}), 200

users = []


@app.route('/api/v1/users', methods=['POST'])
def register_user():
    # registers a  new user
    data = request.get_json()
    user_id = len(users)+1
    registered_on = datetime.now()
    user = User(user_id, data['firstname'], data['lastname'],
                data['othernames'], data['email'], data['phonenumber'],
                data['username'], registered_on)
    users.append(user)
    return jsonify({"message": " account has been successfully created"}), 201


@app.route('/api/v1/users', methods=['GET'])
def fetch_users():
    # fetches all user's records
    user = [user.get_user_details() for user in users]
    return jsonify({"users": user})


@app.route('/api/v1/users/<int:user_id>', methods=['GET'])
# this fetches a single user account
def fetch_single_user_details(user_id):
    fetched_user = []
    user = users[user_id - 1]
    fetched_user.append(user.get_user_details())
    return jsonify({"user": fetched_user}), 200


@app.route('/api/v1/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    # this function enables user to delete his/her account
    if user_id == 0 or user_id > len(users):
        return jsonify({"message": "Index out of range"}), 400
    for user in users:
        if user.user_id == user_id:
            users.remove(user)
    return jsonify({"message": "account successfully deleted"}), 200
