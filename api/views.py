from flask import jsonify, request, abort, Blueprint
from .models import Record, User
from datetime import datetime
import re

record = Blueprint('record', __name__)
user = Blueprint('user', __name__)
records = []

name_regex = r"[a-zA-Z]"
password_regex = r"(?=.*[0-9])"
username_regex = r"[a-zA-Z0-9_]"
phone_regex = r"\d{3}-\d{3}-\d{4}"
record = Blueprint('record', __name__)



@record.route('/api/v1/records', methods=['POST'])
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


@record.route('/api/v1/records', methods=['GET'])
def fetch_record():
    # fetches all user's records
    Records = [record.get_record() for record in records]
    return jsonify({"records": Records}), 200


@record.route('/api/v1/records/<int:record_id>', methods=['GET'])
def fetch_single_record(record_id):
    fetched_record = []
    record = records[record_id - 1]
    fetched_record.append(record.get_record())
    return jsonify({"record": fetched_record}), 200


@record.route('/api/v1/records/<int:record_id>', methods=['PUT'])
def edit_record(record_id):
    # function for editing a record
    if not record_id:
        return jsonify({"message": "Invalid record_id"}), 400
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


@record.route('/api/v1/records/<int:record_id>', methods=['DELETE'])
def delete_record(record_id):
    # this function enables user delete record
    if record_id == 0 or record_id > len(records):
        return jsonify({"message": "Index is out of range"}), 400
    for record in records:
        if record.record_id == record_id:
            records.remove(record)
    return jsonify({"message": "record successfully deleted"}), 200

users = []


@user.route('/api/v1/users', methods=['POST'])
def register_user():
    # registers a  new user
    data = request.get_json()
    user_id = len(users)+1
    registered_on = datetime.now()
    username = data['username']
    text_fields = ['othernames', 'firstname', 'lastname', 'username']
    user_fields = ['othernames', 'firstname', 'lastname']
    key_fields = ['email', 'password']
    for name in user_fields:
        if not re.match(name_regex, data[name]):
            return jsonify({'message': 'Enter correct ' + name + ' format'}), 400
    for text_field in text_fields:
        if len(data[text_field]) > 10:
            return jsonify({'message': text_field + ' too long'}), 404
        
    for key in key_fields:
        if not data[key] or data[key].isspace():
            return jsonify({'message': key + ' field can not be empty.'}), 400   
    if not username or username.isspace():
        return jsonify({'message': 'Username can not be empty.'}), 400 
    if not re.match(r"[^@.]+@[A-Za-z]+\.[a-z]+", data['email']):
        return jsonify({'message': 'Enter a valid email address.'}), 400
    if not re.match(username_regex, data['username']):
        return jsonify({'message': 'Enter a valid username'}), 400
    if not re.match(phone_regex, data['phonenumber']):
        return jsonify({'message': 'Enter phone format 123-456-7890'}), 400
    if len(data['password']) < 8:
        return jsonify({'message': 'Password must be atleast 8 characters'}), 400  
    user = User(user_id, data['firstname'], data['lastname'],
                data['othernames'], data['email'], data['phonenumber'],
                username, registered_on, data['password'])
    users.append(user)
    return jsonify({"message": " account has been successfully created"}), 201


@user.route('/api/v1/users', methods=['GET'])
def fetch_users():
    # fetches all user's records
    user = [user.get_user_details() for user in users]
    return jsonify({"users": user})


@user.route('/api/v1/users/<int:user_id>', methods=['GET'])
# this fetches a single user account
def fetch_single_user_details(user_id):
    fetched_user = []
    try:
        user = users[user_id - 1]
        if user not in users:
            return jsonify({"message": "user doesnot exist"}), 404
        fetched_user.append(user.get_user_details())
        return jsonify({"user": fetched_user}), 200
    except Exception:
        return jsonify({"message": "User not found"}), 404


@user.route('/api/v1/users/login', methods=['POST'])
def login():
    # this function enables user to log in  
    data = request.get_json()
    email = data.get('email')
    #login_details = ['email', 'password', 'username']
    #for detail in login_details:
    for user in users:
        if user.email == email:
            return jsonify({'message': user.get_user_details()}), 200
    return jsonify({'message': 'user not found in list'}), 404

        #if data.get(detail) in users:
            #return jsonify({'message': 'Logged in.'}), 201
              


@user.route('/api/v1/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    # this function enables user to delete his/her account
    if user_id in users == user_id:
            users.remove(user)
    return jsonify({"message": "account successfully deleted"}), 200