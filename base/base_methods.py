import requests
from base.logger import Logger


class BaseMethods:

    @staticmethod
    def get_method(url):
        Logger.add_request(url, method='GET')
        response = requests.get(url, json={}, headers={"Content-Type": "application/json"})
        Logger.add_response(response)
        return response
