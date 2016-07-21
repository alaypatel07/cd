from unittest import TestCase

from left_factoring import get_key, left_factor


class TestLeftFactoring(TestCase):

    def test_group_by(self):
        self.assertEqual("a", get_key("abc"))
        self.assertEqual("b", get_key("bc"))

    def test_left_factor(self):
        test_case = ["abc", "ab", "a", "aab", "aac", "dd", "db"]
        c = left_factor("A", test_case)
        print(c)