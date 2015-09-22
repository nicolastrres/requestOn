import requests


class RequestService():

    def __init__(self):
        # services [{'app': 'Facebook', 'url': 'https://facebook.com', 'status': '200'}]
        self.services = []

    def add_service(self, url):
        self.services.append({'url': url})

    def read_service_from_file(self, file):
        with open(file) as f:
            self.services = f.readlines()

    def call_services(self):
        status_codes = []
        for service in self.services:
            try:
                response = requests.get(service['url'])
                response_status_code = response.status_code
                status_codes.append(response_status_code)
                response.raise_for_status()
            except requests.HTTPError as e:
                print(e)
            except requests.RequestException as e:
                print(e.args)
        return status_codes
