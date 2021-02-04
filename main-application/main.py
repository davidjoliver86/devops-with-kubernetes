import uuid
import logging
import time

LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.INFO)
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter("%(asctime)s: %(message)s"))
LOGGER.addHandler(handler)

def main():
    random_uuid = uuid.uuid4()
    try:
        while True:
            LOGGER.info(random_uuid)
            time.sleep(5)
    except KeyboardInterrupt:
        pass
    

if __name__ == '__main__':
    main()
