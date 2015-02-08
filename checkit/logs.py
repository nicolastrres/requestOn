import logging


class Logs():
    logging.basicConfig(level=logging.INFO)
        
    def info(message):
        logging.info("Calling endpoint: " + message)
        
    def error_status_code(status_code):
        logging.error("Error %s" % status_code)
        
    def general_error(message):
        logging.error("Undefined Error: " + message)
        
    def extra_info(message):
        logging.info("Extra information: " + message)