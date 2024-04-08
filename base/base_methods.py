import requests


class BaseMethods:

    @staticmethod
    def get_method(url):
        response = requests.get(url, json={}, headers={"Content-Type": "application/json"})
        return response
