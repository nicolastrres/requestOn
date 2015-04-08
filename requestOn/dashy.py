import requests


class Dashy():
    def __init__(self, api_name, status_codes):
        self.name = api_name
        self.environment = "test"
        self.status_codes = status_codes
        self.success = create_response_boolean_list(self.status_codes)

    def request(self):
        url = "http://localhost:3000/api/requests/87AB7982EC3D9A799783332B68B3A22E"
        for value in self.success:
            requests.post(url, self.create_value(value))

    def create_value(self, success):
        return {"request[name]": self.name,
                "request[success]": success,
                "request[meta][environment]": "test"}


def create_response_boolean_list(status_codes):
    return [True if response == 200 else False for response in status_codes]
