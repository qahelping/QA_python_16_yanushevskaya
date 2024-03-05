import requests
import logging
import sys


def create_logger():
    logger = logging.getLogger()
    logger_level = sys.argv[1]
    if logger_level == "INFO":
        logger.setLevel(logging.INFO)
    elif logger_level == "ERROR":
        logger.setLevel(logging.ERROR)
    print(logger_level)
    return logger


logger = create_logger()


def delete(url):
    try:
        response = requests.delete(url)
        response.raise_for_status()
        logger.info("OK. URL: %s, Code: %d", url, response.status_code)
        return response.content
    except requests.exceptions.RequestException as e:
        logger.error("Error. %s", str(e))
        return None


response_content = delete("https://httpbin.org/status/404")
response_content2 = delete("https://httpbin.org/status/202")
