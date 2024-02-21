import logging
import sys

import requests


def create_logger():
    logger = logging.getLogger()

    formatter = logging.Formatter('%(asctime)s - %(message)s')
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    loger_level = sys.argv[2]
    print(loger_level)

    if loger_level == 'INFO':
        logger.setLevel(logging.INFO)
    if loger_level == 'ERROR':
        logger.setLevel(logging.ERROR)
    if loger_level == 'CRITICAL':
        logger.setLevel(logging.CRITICAL)
    if loger_level == 'WARNING':
        logger.setLevel(logging.WARNING)


    logger.addHandler(console_handler)
    return logger


logger = create_logger()
