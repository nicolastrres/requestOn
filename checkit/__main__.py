import argparse
from request_service import RequestService


def parse_args():
    parser = argparse.ArgumentParser(prog="Checkit")
    group_request = parser.add_argument_group("Request options")
    group_request.add_argument("-r", "--request", action="store", dest="request_url", help="Do a request to an specific url")
    args = parser.parse_args()

    return args


def main():
    requestService = RequestService()
    args = parse_args()
    if args.request_url:
        requestService.getcode(url=args.request_url)

if __name__ == "__main__":
    main()

