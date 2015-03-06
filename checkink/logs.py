import logging


class Logs():
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)

    def write_file(self, filename):
        self.logger.addHandler(logging.FileHandler(filename))

    def info(self, message):
        self.logger.info('Calling endpoint: ' + message)

    def error_status_code(self, status_code):
        self.logger.error('Error %s' % status_code)

    def general_error(self, message):
        self.logger.error('Undefined Error: ' + message)

    def extra_info(self, message):
        self.logger.info('Extra information: ' + message)
