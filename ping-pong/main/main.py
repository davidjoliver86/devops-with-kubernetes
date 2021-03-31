import uuid
import datetime
import os

from flask import Flask

# Globals
app = Flask(__name__)
counter = 0

@app.route('/')
def main():
    global counter
    counter += 1
    return str(counter)
