import uuid
import datetime
import os

from flask import Flask

# Globals
app = Flask(__name__)
random_uuid = uuid.uuid4()

@app.route("/")
def hello():
    return f"{random_uuid}\n{datetime.datetime.now().isoformat()}"
