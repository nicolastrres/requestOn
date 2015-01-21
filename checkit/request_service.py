import urllib.request
import urllib.error
import urllib.parse
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-r", "--request", dest="getcode",
                  help="send a request to a website", metavar="REQUEST")
parser.add_option("-q", "--quiet",
                  action="store_false", dest="verbose", default=True,
                  help="don't print status messages to stdout")

(options, args) = parser.parse_args()

class RequestService():

    def getcode(self, url):
        try:
            return urllib.request.urlopen(url).getcode()
        except urllib.error.HTTPError as e:
            return e.code
        except urllib.error.URLError as e:
            return e.args

if __name__ == "__main__":
    request_service = RequestService()
