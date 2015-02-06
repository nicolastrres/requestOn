import logging


class Logs():
    def log(self):
        logging.basicConfig(filename='example.log', level=logging.DEBUG)
        logging.debug('This message should go to the log file')
        logging.info('So should this')
        logging.warning('And this, too')


if __name__ == "__main__":
    logs = Logs()
    logs.log()
