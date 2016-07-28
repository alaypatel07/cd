from unittest import TestCase

from left_factoring import get_key, left_factor, get_left_factored


class TestLeftFactoring(TestCase):

    def test_group_by(self):
        self.assertEqual("a", get_key("abc"))
        self.assertEqual("b", get_key("bc"))

    def test_left_factor(self):
        test_case = ["abc", "ab", "a", "aab", "aac", "dd", "db"]
        expected_output = {
            "A": [
                    "aA'",
                    "dA''"
            ],
            "A'" :[
                "bc",
                "b",
                "",
                "ab",
                "ac"
            ],
            "A''": [
                "d",
                "b"
            ]
        }
        g = left_factor("A", test_case)
        for key in g:
            if key not in expected_output:
                self.fail("Key not in Output")

    def test_get_left_factored(self):
        test_case = ["abc", "ab", "a", "aab", "aac", "dd", "db"]
        expected_output = {"A''": ['', "bA'''", "aA''''"], "A'": ['d', 'b'], "A''''": ['b', 'c'], 'A': ["dA'", "aA''"],
                           "A'''": ['c', '']}
        for key in get_left_factored(dict(A=test_case)):
            if key not in expected_output:
                self.fail()