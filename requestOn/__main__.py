import ast
import sys
import argparse

from request_service import RequestService
from dashy import Dashy


def usage():
    print("\t\t\t\t\t RequestOn\n\n")
    print("Usage: requestOn -t targets\n")
    print("-t --targets \t\t\t- targets to be requested. If file is defined, "
          "this will not be consider. Optional")
    # print("-f --file                  - file with endpoints to read and to be requested. Optional")
    # print("-a --appid                 - Appid in dashy. Optional")
    print("\n\nExamples:\n requestOn -t \"{'url': 'https://google.com', time: 300}\""
          " \"{'url': 'https://facebook.com', time: 100}\"\n\n")
    sys.exit(0)


def parse_args():
    parser = argparse.ArgumentParser(prog="RequestOn")
    group_request = parser.add_argument_group("Request options")
    group_request.add_argument("-t", "--targets", nargs="*", type=str, default='', action="store", dest="target_url",
                               help="Do a requests to a list of targets")
    # group_request.add_argument("-f", "--file", action="store", dest=" file_to_read",
    #                            help="file with endpoints to read and to be requested. Optional")
    # group_dashy = parser.add_argument_group("Dashy options")
    # group_dashy.add_argument("-a", "--appid", action="store", dest="app_id",
    #                          help="Specify the app id in dashy")
    # group_dashy.add_argument("-n", "--name", action="store", dest="api_name",
    #                          help="Specify the api name in dashy")
    args = parser.parse_args()
    return args


def main():
    request_service = RequestService()
    status_codes = []

    if not len(sys.argv[1:]):
        usage()
    args = parse_args()

    if args.target_url:
        for target in args.target_url:
            url = ast.literal_eval(target)['url']
            request_service.add_service(url)

        status_codes = request_service.call_services()
        call_dashy(status_codes=status_codes)

    # elif args.file_to_read:
    #     request_service.read_endpoints_from_file(args.file_to_read)
    #     status_codes = request_service.call_endpoints()
    #     call_dashy(status_codes=status_codes, args=args)
    print(status_codes)


def call_dashy(status_codes):
    dashy = Dashy(app_id="87AB7982EC3D9A799783332B68B3A22E", app_name="Teste basico", status_codes=status_codes)
    dashy.request()

if __name__ == "__main__":
    main()
