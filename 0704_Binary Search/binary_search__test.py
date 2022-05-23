import unittest

from dataclasses import dataclass
from binary_search import Solution1

import time

total_loop = 1000
print("total_loop= ", total_loop)


@dataclass
class TestData:
    nums: None
    target: int
    ans: int


def generate_data():
    data = [TestData([-1, 0, 3, 5, 9, 12], 9, 4),
            TestData([-1, 0, 3, 5, 9, 12], 2, -1),
            ]

    return data


class TestSol1(unittest.TestCase):

    def setUp(self):
        self.args = (generate_data())
        # print("self.args= ", self.args)

    def tearDown(self):
        self.args = None

    def test_search(self):

        time_start = time.process_time()

        for count in range(total_loop):
            for arg in self.args:
                expected = arg.ans
                s1 = Solution1()
                actual = s1.search(arg.nums, arg.target)
                self.assertEqual(expected, actual)

        time_end = time.process_time()

        print("Solution1 runtime= ", time_end - time_start)


if __name__ == '__main__':
    unittest.main()
