import requests

from main import logger


class BaseServices:

    def path(self, url, headers=None, body=None):
        response = requests.patch(url, headers=headers, data=body)
        if response.status_code == 200:
            logger.info("OK")
        else:
            logger.error("FAIL")
            assert False
        return response

    def get(self, url, headers=None, body=None):
        response = requests.patch(url, headers=headers, data=body)
        if response.status_code == 200:
            logger.info("OK")
        else:
            logger.error("FAIL")
            assert False
        return response
