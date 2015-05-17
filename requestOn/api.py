from .logs import Logs


class API(object):
    def __init__(self, api_name="", app_id=""):
        self.api_name = api_name
        self.app_id = app_id
        self.logs = Logs()
