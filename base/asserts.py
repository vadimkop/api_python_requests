import json
from requests import Response
import pytest_check as check


class Asserts:

    @staticmethod
    def status_code(response: Response, status_code):
        check.equal(status_code, response.status_code, f"URL: {response.url}. "
                                                       f"Error: unexpected status code - {response.status_code}")

    @staticmethod
    def response_parameters(response: Response, expected_parameters):
        parameters = json.loads(response.text)
        check.less_equal(set(expected_parameters), set(list(parameters)), f"URL: {response.url}. Error: All or part "
                                                                          f"of the required parameters are missing")

    @staticmethod
    def response_values(response: Response, parameter, expected_value):
        check_value = response.json().get(parameter)
        check.equal(expected_value, check_value, f"URL: {response.url}. Error: unexpected value")