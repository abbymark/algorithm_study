from . import 3
import unittest

class Test3(unittest.TestCase):
    def test_lengthOfLongestSubstring(self):
        self.assertEqual(3.lengthOfLongestSubstring('abcabcbb'), 3)