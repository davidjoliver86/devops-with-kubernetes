import os

from flask import Flask

app = Flask(__name__)

PORT = os.environ.get("FLASK_RUN_PORT", 5000)


@app.route("/")
def hello():
    return f"Server started in port {PORT}"
