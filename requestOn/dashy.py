import requests


class Dashy():
    def __init__(self, api, status_codes):
        self.api = api
        self.environment = "test"
        self.status_codes = status_codes
        self.boolean_response_list = create_response_boolean_list(self.status_codes)

    def request(self):
        url = "http://localhost:3000/api/requests/{}".format(self.api.app_id)
        for value in self.boolean_response_list:
            requests.post(url, self.create_value(value))

    def create_value(self, success):
        return {"request[name]": self.api.api_name,
                "request[success]": success,
                "request[meta][environment]": "test"}


def create_response_boolean_list(status_codes):
    return [True if response == 200 else False for response in status_codes]
