import urllib.request
import urllib.error
import urllib.parse
import sys
import os.path

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from checkit.logs import Logs


class RequestService():

    def __init__(self, api_name):
        self.api_name = api_name

    def get_code(self, url):
        try:
            code = urllib.request.urlopen(url).getcode()
            Logs.info(url + " --- code response:" + str(code))
            return code
        except urllib.error.HTTPError as e:
            Logs.error_status_code(e.code)
            return e.code
        except urllib.error.URLError as e:
            Logs.general_error(e.reason)
            return e.reason
        except ValueError as e:
            Logs.general_error("".join(e.args))
            return e.args

    def addEndpoints(self, endpointsList):
        self.endpoints = endpointsList

    def getEndpointList(self):
        return self.endpoints

    def start(self):
        responses = []
        for endpoint in self.endpoints:
            try:
                code = urllib.request.urlopen(endpoint).getcode()
                responses.append(code)
                Logs.info(endpoint + " --- code response:" + str(code))
            except urllib.error.HTTPError as e:
                Logs.error_status_code(e.code)
                responses.append(e.code)
            except urllib.error.URLError as e:
                Logs.general_error(e.reason)
                responses.append(0)
            except ValueError as e:
                Logs.general_error("".join(e.args))
                responses.append(0)

        return responses
