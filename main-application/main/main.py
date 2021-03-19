import uuid
# import logging
import datetime

# LOGGER = logging.getLogger(__name__)
# LOGGER.setLevel(logging.INFO)
# handler = logging.StreamHandler()
# handler.setFormatter(logging.Formatter("%(asctime)s: %(message)s"))
# LOGGER.addHandler(handler)

# def main():
#     random_uuid = uuid.uuid4()
#     try:
#         while True:
#             LOGGER.info(random_uuid)
#             time.sleep(5)
#     except KeyboardInterrupt:
#         pass


# if __name__ == '__main__':
#     main()


import os

from flask import Flask

# Globals
app = Flask(__name__)
random_uuid = uuid.uuid4()

@app.route("/")
def hello():
    return f"{random_uuid}\n{datetime.datetime.now().isoformat()}"
