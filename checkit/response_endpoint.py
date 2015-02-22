class ResponseEndpoint(object):

    code = 0
    data = ''

    def __init__(self, code, data):
        self.code = code
        self.data = data
