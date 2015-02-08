import urllib.request
import urllib.error
import urllib.parse
from checkit.logs import Logs


class RequestService():
    
    def getcode(self, url):
        try:
            Logs.info(url)
            return urllib.request.urlopen(url).getcode()
        except urllib.error.HTTPError as e:
            Logs.error_status_code(e.code)
            return e.code
        except urllib.error.URLError as e:
            Logs.general_error(e.reason)
            return e.reason
        except ValueError as e:
            Logs.general_error("".join(e.args))
            return e.args
