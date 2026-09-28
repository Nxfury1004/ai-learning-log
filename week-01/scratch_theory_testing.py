import unittest

class BuggySurvey:
    responses = []                 # class attribute: ONE list shared by every instance
    def __init__(self, question):
        self.question = question
    def store_response(self, r):
        self.responses.append(r)

class FixedSurvey:
    def __init__(self, question):
        self.question = question
        self.responses = []        # instance attribute: a fresh list per instance
    def store_response(self, r):
        self.responses.append(r)

class TestSurveys(unittest.TestCase):
    def setUp(self):
        print(f"  setUp() runs; this test object's id = {id(self)}")

    def test_fixed_instances_are_independent(self):
        a, b = FixedSurvey("q"), FixedSurvey("q")
        a.store_response("English")
        self.assertEqual(b.responses, [])

    def test_buggy_instances_are_independent(self):
        a, b = BuggySurvey("q"), BuggySurvey("q")
        a.store_response("English")
        self.assertEqual(b.responses, [])

print("__name__ is:", __name__)
if __name__ == "__main__":
    unittest.main(verbosity=2)
