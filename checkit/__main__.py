import argparse

def parse_args(req_args=None):
    parser = argparse.ArgumentParser(prog="Checkit")
    group_request = parser.add_argument_group("Request options")
    group_request.add_argument("-r", "--request", action="store", type="string", destination="request_url")

    args = parser.parse_args(req_args)
    return args


def main(req_args=None):
    args = parse_args(req_args)