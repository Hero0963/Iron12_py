import unittest
from dataclasses import dataclass
from typing import List
from move_zeroes import Solution1
from move_zeroes import Solution2
import time

total_loop = 1000
print("total_loop= ", total_loop)


@dataclass
class TestData:
    nums: List[int]
    ans: List[int]


def generate_data():
    data = [TestData([0, 1, 0, 3, 12], [1, 3, 12, 0, 0]),
            TestData([0], [0]),
            ]

    return data


class TestSol1(unittest.TestCase):

    def setUp(self):
        self.args = (generate_data())
        # print("self.args= ", self.args)

    def tearDown(self):
        self.args = None

    def test_moveZeroes(self):

        time_start = time.process_time()

        for count in range(total_loop):
            for arg in self.args:
                expected = arg.ans
                s = Solution1()
                actual = s.moveZeroes(arg.nums)
                self.assertEqual(expected, actual)

        time_end = time.process_time()

        print(self.__class__.__name__ + " runtime= ", time_end - time_start)


if __name__ == '__main__':
    unittest.main()
