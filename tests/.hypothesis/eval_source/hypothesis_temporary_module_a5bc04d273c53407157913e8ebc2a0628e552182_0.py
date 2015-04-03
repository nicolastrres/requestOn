from hypothesis.utils.conventions import not_set

def accept(f):
    def test_responses_should_be_transform_to_boolean(self, responses_list=not_set):
        return f(self=self, responses_list=responses_list)
    return test_responses_should_be_transform_to_boolean
