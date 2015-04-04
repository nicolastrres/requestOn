import argparse
import sys
from request_service import RequestService
from logs import Logs
from dashy import Dashy


def usage():
    print("\t\t\t RequestOn\n\n")
    print("Usage: requestOn -r target [-l log_file_name]")
    print("-t --target                  - target to be requested. If file is defined, "
          "this will not be consider. Optional")
    print("-f --file                  - file with endpoints to read and to be requested. Optional")
    print("-l --log                     - name of the file where the logs are going to be saved. Optional")
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
    args = parser.parse_args()
    return args


def main():
    logs = Logs()
    requestService = RequestService(api_name="Api_name", logs=logs)

    if not len(sys.argv[1:]):
        usage()
    args = parse_args()

    if args.log_file_name:
        logs.write_file(filename=args.log_file_name)
    if args.target_url:
        requestService.add_endpoints(args.target_url)
        responses = requestService.start()
        print(responses)
    elif args.file_to_read:
        requestService.read_endpoints_from_file(args.file_to_read)
        responses = requestService.start()
        print(responses)

if __name__ == "__main__":
    main()
