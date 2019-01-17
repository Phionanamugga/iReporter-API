from flask import Flask
from api.views import record, user

app = Flask(__name__)
app.register_blueprint(record)
app.register_blueprint(user)
