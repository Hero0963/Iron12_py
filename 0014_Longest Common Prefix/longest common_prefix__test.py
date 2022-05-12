import unittest

from dataclasses import dataclass
from longest_common_prefix import Solution1

import time

total_loop = 1000
print("total_loop= ", total_loop)


@dataclass
class TestData:
    strs: None
    ans: str


def generate_data():
    data = [TestData(["flower", "flow", "flight"], "fl"),
            TestData(["dog", "racecar", "car"], ""),
            ]

    return data


class TestSol1(unittest.TestCase):

    def setUp(self):
        self.args = (generate_data())
        # print("self.args= ", self.args)

    def tearDown(self):
        self.args = None

    def test_longestCommonPrefix(self):

        time_start = time.process_time()

        for count in range(total_loop):
            for arg in self.args:
                expected = arg.ans
                s1 = Solution1()
                actual = s1.longestCommonPrefix(arg.strs)
                self.assertEqual(expected, actual)

        time_end = time.process_time()

        print("Solution1 runtime= ", time_end - time_start)


if __name__ == '__main__':
    unittest.main()
