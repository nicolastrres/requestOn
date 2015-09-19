import random
import unittest
from requestOn.dashy import create_response_boolean_list, map_to_dashy

possible_responses = [200, 400, 401, 404, 405, 406, 500, 501, 502, 503, None, 0]
boolean_responses = [True, False, False, False, False, False, False, False, False, False, False, False]


class DashyTest(unittest.TestCase):

    def test_responses_should_be_transformed_to_boolean(self):
        response_list = generate_response_list(length=10)
        response_boolean_list = create_response_boolean_list(response_list)
        for response in response_boolean_list:
            self.assertTrue(type(response) is bool)

    def test_responses_should_be_empty_if_array_is_empty(self):
        response_list = []
        response_boolean_list = create_response_boolean_list(response_list)
        self.assertEqual(0, len(response_boolean_list))

    def test_responses_should_be_transformed_to_right_boolean(self):
        response_list = possible_responses
        expected_responses = boolean_responses
        response_boolean_list = create_response_boolean_list(response_list)
        self.assertListEqual(expected_responses, response_boolean_list)

    def test_map_to_dashy(self):
        app_name = 'REQUEST'
        boolean_response = True
        expected_map = {"request[name]": app_name,
                        "request[success]": boolean_response,
                        "request[meta][environment]": "test"}

        actual_map = map_to_dashy(app_name=app_name, value=boolean_response)
        self.assertDictEqual(expected_map, actual_map)


def think_in_a_number(max_number):
    return random.randint(0, max_number)


def give_me_a_response():
    return random.choice(possible_responses)


def generate_response_list(length):
    response_list = []
    for i in range(0, think_in_a_number(length)):
        response_list.append(give_me_a_response())
    return response_list
