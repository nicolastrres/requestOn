import argparse
import sys
from api import API
from request_service import RequestService
from dashy import Dashy


def usage():
    print("\t\t\t RequestOn\n\n")
    print("Usage: requestOn -r target")
    print("-t --target                - target to be requested. If file is defined, "
          "this will not be consider. Optional")
    print("-f --file                  - file with endpoints to read and to be requested. Optional")
    print("-a --appid                 - Appid in dashy. Optional")
    print("-n --name                  - API name in dashy. Optional")
    print("\n\nExamples:\n requestOn -t http://www.google.com")
    print(" requestOn -t http://www.facebook.com -l")
    sys.exit(0)


def parse_args():
    parser = argparse.ArgumentParser(prog="RequestOn")
    group_request = parser.add_argument_group("Request options")
    group_request.add_argument("-t", "--targets", nargs="*", type=str, default=[], action="store", dest="target_url",
                               help="Do a requests to a list of targets")
    group_request.add_argument("-f", "--file", action="store", dest="file_to_read",
                               help="file with endpoints to read and to be requested. Optional")
    group_dashy = parser.add_argument_group("Dashy options")
    group_dashy.add_argument("-a", "--appid", action="store", dest="app_id",
                             help="Specify the app id in dashy")
    group_dashy.add_argument("-n", "--name", action="store", dest="api_name",
                             help="Specify the api name in dashy")
    args = parser.parse_args()
    return args


def main():
    request_service = RequestService()

    if not len(sys.argv[1:]):
        usage()
    args = parse_args()

    if args.target_url:
        request_service.endpoints = args.target_url
        status_codes = request_service.call_endpoints()
        call_dashy(status_codes=status_codes, args=args)
    elif args.file_to_read:
        request_service.read_endpoints_from_file(args.file_to_read)
        status_codes = request_service.call_endpoints()
        call_dashy(status_codes=status_codes, args=args)


def call_dashy(status_codes, args):
    if args.app_id:
        api_name = args.api_name if args.api_name else ""
        api = API(api_name=api_name, app_id=args.app_id)
        dashy = Dashy(api=api, status_codes=status_codes)
        dashy.request()
    print(status_codes)

if __name__ == "__main__":
    main()
