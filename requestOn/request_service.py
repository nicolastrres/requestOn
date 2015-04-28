import requests


class RequestService():

    def __init__(self, logs):
        self.endpoints = []
        self.logs = logs

    def add_endpoint(self, endpoint):
        self.endpoints.append(endpoint)

    def add_endpoints(self, endpointsList):
        self.endpoints = endpointsList

    def get_endpointList(self):
        return self.endpoints

    def read_endpoints_from_file(self, file):
        with open(file) as f:
            self.add_endpoints(f.readlines())

    def call_endpoints(self):
        status_codes = []
        for endpoint in self.endpoints:
            try:
                response = requests.get(endpoint)
                response_status_code = response.status_code
                status_codes.append(response_status_code)
                self.logs.info(endpoint + " --- code response:" + str(response_status_code))
                response.raise_for_status()
            except requests.HTTPError as e:
                self.logs.general_error(e)
            except requests.RequestException as e:
                self.logs.general_error(e.args)
        return status_codes
