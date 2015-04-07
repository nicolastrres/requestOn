import requests

class Dashy():
    def request(self, requestService, responses):
        url = "http://localhost:3000/api/requests/87AB7982EC3D9A799783332B68B3A22E"
        for index, response in enumerate(responses):
            responses[index] = True if response == 200 else False

        for code in responses:
            values = {"request[name]": requestService.api_name,
                      "request[success]": code,
                      "request[meta][environment]": "test"}
            req = requests.post(url, values)
            print(req.status_code)

if __name__ == '__main__':
    dashy = Dashy()
