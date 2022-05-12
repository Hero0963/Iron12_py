import unittest

from dataclasses import dataclass
from roman_to_integer import Solution1
from roman_to_integer import Solution2

import time

total_loop = 1000
print("total_loop= ", total_loop)


@dataclass
class TestData:
    s: str
    ans: None


def generate_data():
    data = [TestData("III", 3),
            TestData("LVIII", 58),
            TestData("MCMXCIV", 1994)
            ]

    return data


class TestSol1(unittest.TestCase):

    def setUp(self):
        self.args = (generate_data())
        # print("self.args= ", self.args)

    def tearDown(self):
        self.args = None

    def test_romanToInt(self):

        time_start = time.process_time()

        for count in range(total_loop):
            for arg in self.args:
                expected = arg.ans
                s1 = Solution1()
                actual = s1.romanToInt(arg.s)
                self.assertEqual(expected, actual)

        time_end = time.process_time()

        print("Solution1 runtime= ", time_end - time_start)


class TestSol2(unittest.TestCase):

    def setUp(self):
        self.args = (generate_data())
        # print("self.args= ", self.args)

    def tearDown(self):
        self.args = None

    def test_romanToInt(self):

        time_start = time.process_time()

        for count in range(total_loop):
            for arg in self.args:
                expected = arg.ans
                s2 = Solution2()
                actual = s2.romanToInt(arg.s)
                self.assertEqual(expected, actual)

        time_end = time.process_time()

        print("Solution2 runtime= ", time_end - time_start)


if __name__ == '__main__':
    unittest.main()
