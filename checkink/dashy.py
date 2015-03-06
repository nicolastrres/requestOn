import urllib.request
import urllib.error
import urllib.parse


class DashyIntegration():
    def request(self):
        url = "http://localhost:3000/api/requests/87AB7982EC3D9A799783332B68B3A22E"
        values = {"request[name]": "agustin",
                  "request[success]": "false",
                  "request[meta][environment]": "test"}
        data = urllib.parse.urlencode(values)
        binary_data = data.encode('utf8')
        req = urllib.request.Request(url, binary_data)
        print(urllib.request.urlopen(req).getcode())

if __name__ == '__main__':
    dashy = DashyIntegration()
    dashy.request()
