import urllib.request
import urllib.error
import urllib.parse


class Dashy():
    def request(self, request_service, responses):
        url = "http://localhost:3000/api/requests/87AB7982EC3D9A799783332B68B3A22E"
        responses = create_response_boolean_list(responses)

        for code in responses:
            values = self.create_values(request_service.api_name, code)
            data = urllib.parse.urlencode(values)
            binary_data = data.encode('utf8')
            urllib.request.Request(url, binary_data)

    def create_values(self, api_name, code):
        return {"request[name]": api_name,
                "request[success]": code,
                "request[meta][environment]": "test"}


def create_response_boolean_list(responses):
    return [True if response == 200 else False for response in responses]
