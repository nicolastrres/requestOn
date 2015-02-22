import logging


class Logs():
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    @staticmethod
    def info(message):
        Logs.logger.info('Calling endpoint: ' + message)

    @staticmethod
    def error_status_code(status_code):
        Logs.logger.error('Error %s' % status_code)

    @staticmethod
    def general_error(message):
        Logs.logger.error('Undefined Error: ' + message)

    @staticmethod
    def extra_info(message):
        Logs.logger.info('Extra information: ' + message)
