import argparse
import sys
from api import API
from request_service import RequestService
from dashy import Dashy


def usage():
    print("\t\t\t RequestOn\n\n")
    print("Usage: requestOn -r target [-l log_file_name]")
    print("-t --target                - target to be requested. If file is defined, "
          "this will not be consider. Optional")
    print("-f --file                  - file with endpoints to read and to be requested. Optional")
    print("-l --log                   - name of the file where the logs are going to be saved. Optional")
    print("-a --appid                 - Appid in dashy. Optional")
    print("-n --name                  - API name in dashy. Optional")
    print("\n\nExamples:\n requestOn -t http://www.google.com")
    print(" requestOn -t http://www.facebook.com -l logs.txt")
    sys.exit(0)


def parse_args():
    parser = argparse.ArgumentParser(prog="RequestOn")
    group_request = parser.add_argument_group("Request options")
    group_request.add_argument("-t", "--targets", nargs="*", type=str, default=[], action="store", dest="target_url",
                               help="Do a requests to a list of targets")
    group_request.add_argument("-f", "--file", action="store", dest="file_to_read",
                               help="file with endpoints to read and to be requested. Optional")
    group_log = parser.add_argument_group("Logs options")
    group_log.add_argument("-l", "--log", action="store", dest="log_file_name",
                           help="Specify a log filename")
    group_dashy = parser.add_argument_group("Dashy options")
    group_dashy.add_argument("-a", "--appid", action="store", dest="app_id",
                             help="Specify the app id in dashy")
    group_dashy.add_argument("-n", "--name", action="store", dest="api_name",
                             help="Specify the api name in dashy")
    args = parser.parse_args()
    return args


def main():
    api = API("test re loco")
    request_service = RequestService(logs=api.logs)

    if not len(sys.argv[1:]):
        usage()
    args = parse_args()

    if args.log_file_name:
        api.logs.write_file(filename=args.log_file_name)
    if args.target_url:
        request_service.add_endpoints(args.target_url)
        status_codes = request_service.call_endpoints()
        if args.app_id:
            api_name = args.api_name if args.api_name else ""
            api = API(api_name=api_name, app_id=args.app_id)
            dashy = Dashy(api=api, status_codes=status_codes)
            dashy.request()
        print(status_codes)
    elif args.file_to_read:
        request_service.read_endpoints_from_file(args.file_to_read)
        status_codes = request_service.call_endpoints()
        if args.app_id:
            api_name = args.api_name if args.api_name else ""
            api = API(api_name=api_name, app_id=args.app_id)
            dashy = Dashy(api=api, status_codes=status_codes)
            dashy.request()
        print(status_codes)

if __name__ == "__main__":
    main()
