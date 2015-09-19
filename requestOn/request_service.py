import ast
import requests


def url(target):
    return target['url']


class RequestService():

    def __init__(self):
        self.endpoints = []

    def add_endpoints(self, args):
        for target in args.target_url:
            self.endpoints.append(url(ast.literal_eval(target)))

    def read_endpoints_from_file(self, file):
        with open(file) as f:
            self.endpoints = f.readlines()

    def call_endpoints(self):
        status_codes = []
        for endpoint in self.endpoints:
            try:
                response = requests.get(endpoint)
                response_status_code = response.status_code
                status_codes.append(response_status_code)
                response.raise_for_status()
            except requests.HTTPError as e:
                print(e)
            except requests.RequestException as e:
                print(e.args)
        return status_codes
