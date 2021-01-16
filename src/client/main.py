import logging

import os
print(os.getcwd())
print(os.listdir())

from client import client



log = logging.getLogger(__name__)

def main():
    logging.basicConfig()
    logging.getLogger("").setLevel(logging.INFO)
    log.info("Starting client")

    client.main()

    log.info("Ending client")


if __name__ == "__main__":
    main()

