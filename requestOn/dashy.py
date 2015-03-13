import urllib.request
import urllib.error
import urllib.parse


class Dashy():
    def request(self, requestService, responses):
        url = "http://localhost:3000/api/requests/87AB7982EC3D9A799783332B68B3A22E"
        for index, response in enumerate(responses):
            responses[index] = True if response == 200 else False

        for code in responses:
            values = {"request[name]": requestService.api_name,
                      "request[success]": code,
                      "request[meta][environment]": "test"}
            data = urllib.parse.urlencode(values)
            binary_data = data.encode('utf8')
            req = urllib.request.Request(url, binary_data)
            print(urllib.request.urlopen(req).getcode())

if __name__ == '__main__':
    dashy = Dashy()
