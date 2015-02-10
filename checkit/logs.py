import logging


class Logs():
    logging.basicConfig(level=logging.INFO)

    @staticmethod
    def info(message):
        logging.info("Calling endpoint: " + message)

    @staticmethod
    def error_status_code(status_code):
        logging.error("Error %s" % status_code)

    @staticmethod
    def general_error(message):
        logging.error("Undefined Error: " + message)

    @staticmethod
    def extra_info(message):
        logging.info("Extra information: " + message)
