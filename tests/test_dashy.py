import random
import unittest
from dashy import create_response_boolean_list

possible_responses = [200, 400, 401, 404, 405, 406, 500, 501, 502, 503, None, 0]


class DashyTest(unittest.TestCase):

    def test_responses_should_be_transform_to_boolean(self):
        response_list = generate_response_list(10)
        print(create_response_boolean_list(response_list))
        print(response_list)


def think_in_a_number(max_number):
    return random.randint(0, max_number)


def give_me_a_response():
    return random.choice(possible_responses)


def generate_response_list(length):
    response_list = []
    for i in range(0, think_in_a_number(length)):
        response_list.append(give_me_a_response())
    return response_list