import argparse
from request_service import RequestService
from logs import Logs


def parse_args():
    parser = argparse.ArgumentParser(prog="Checkit")
    group_request = parser.add_argument_group("Request options")
    group_request.add_argument("-r", "--request", action="store", dest="request_url",
                               help="Do a request to an specific url")
    group_log = parser.add_argument_group("Logs options")
    group_log.add_argument("-l", "--log", action="store", dest="log_file_name",
                           help="Specify a log filename")
    args = parser.parse_args()

    return args


def main():
    requestService = RequestService()
    args = parse_args()
    if args.log_file_name:
        logs.write_file(filename=args.log_file_name)
    if args.request_url:
        requestService.get_code(url=args.request_url, logs=logs)


if __name__ == "__main__":
    logs = Logs()
    main()
