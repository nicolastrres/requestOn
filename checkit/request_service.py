import urllib.request
import urllib.error
import urllib.parse


class RequestService():

    def getcode(self, url):
        try:
            return urllib.request.urlopen(url).getcode()
        except urllib.error.HTTPError as e:
            return e.code
        except urllib.error.URLError as e:
            return e.args
