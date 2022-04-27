import unittest
import substring as st

class Test_TestValue(unittest.TestCase):

    def test_1(self):
        str = "abcabcbb"
        actualLength = st.longestSubstr(str)
        expectedLength = 3
        self.assertEqual(actualLength, expectedLength)

    def test_2(self):
        str = "bbbbb"
        actualLength = st.longestSubstr(str)
        expectedLength = 1
        self.assertEqual(actualLength, expectedLength)

    def test_3(self):
        str = ""
        actualLength = st.longestSubstr(str)
        expectedLength = 0
        self.assertEqual(actualLength, expectedLength)

    def test_4(self):
        str = "pccmesk"
        actualLength = st.longestSubstr(str)
        expectedLength = 5
        self.assertEqual(actualLength, expectedLength)

    def test_5(self):
        str = "cover__   rewrw   "
        actualLength = st.longestSubstr(str)
        expectedLength = 6
        self.assertEqual(actualLength, expectedLength)