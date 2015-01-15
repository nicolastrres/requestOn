import urllib.request, urllib.error, urllib.parse

class RequestService():
    def __init__(self):
        pass

    def getcode(url):
        return urllib.request.urlopen(url).getcode()