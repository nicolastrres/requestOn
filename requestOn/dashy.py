import requests


class Dashy():
    def __init__(self, app_id, app_name, status_codes):
        self.app_id = app_id
        self.app_name = app_name
        self.environment = "test"
        self.status_codes = status_codes
        self.boolean_response_list = create_response_boolean_list(self.status_codes)

    def request(self):
        url = "http://localhost:3000/api/requests/{}".format(self.app_id)
        for value in self.boolean_response_list:
            requests.post(url, map_to_dashy(app_name=self.app_name, value=value))


def map_to_dashy(app_name, value):
    return {"request[name]": app_name,
            "request[success]": value,
            "request[meta][environment]": "test"}


def create_response_boolean_list(status_codes):
    return [True if response == 200 else False for response in status_codes]
