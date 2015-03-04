import logging


class Logs():
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)

    def write_file(self, filename):
        fh = logging.FileHandler(filename)
        fh.setLevel(logging.DEBUG)
        self.logger.addHandler(fh)

    def info(self, message):
        print(message)
        self.logger.info('Calling endpoint: ' + message)
        print(self.logger.handlers)

    def error_status_code(self, status_code):
        self.logger.error('Error %s' % status_code)

    @staticmethod
    def general_error(self, message):
        self.logger.error('Undefined Error: ' + message)

    @staticmethod
    def extra_info(self, message):
        self.logger.info('Extra information: ' + message)
