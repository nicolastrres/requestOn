import urllib.request
import urllib.error
import urllib.parse


class RequestService():

    def __init__(self, api_name, logs):
        self.api_name = api_name
        self.endpoints = []
        self.logs = logs

    def addEndpoint(self, endpoint):
        self.endpoints.append(endpoint)

    def addEndpoints(self, endpointsList):
        self.endpoints = endpointsList

    def getEndpointList(self):
        return self.endpoints

    def start(self):
        responses = []
        for endpoint in self.endpoints:
            try:
                response_endpoint = urllib.request.urlopen(endpoint).getcode()
                responses.append(response_endpoint)
                self.logs.info(endpoint + " --- code response:" + str(response_endpoint))
            except urllib.error.HTTPError as e:
                self.logs.error_status_code(e.code)
                responses.append(e.code)
            except urllib.error.URLError as e:
                self.logs.general_error(e.reason)
                responses.append(0)
            except ValueError as e:
                self.logs.general_error("".join(e.args))
                responses.append(0)

        return responses
