import unittest
from dataclasses import dataclass
from typing import List

from n_repeated_element_in_size_2n_array import Solution1
from n_repeated_element_in_size_2n_array import Solution2
import time

total_loop = 1000
print("total_loop= ", total_loop)


@dataclass
class TestData:
    nums: List[int]
    ans: int


def generate_data():
    data = [TestData([1, 2, 3, 3], 3),
            TestData([2, 1, 2, 5, 3, 2], 2),
            TestData([5, 1, 5, 2, 5, 3, 5, 4], 5),
            ]

    return data


class TestSol1(unittest.TestCase):

    def setUp(self):
        self.args = (generate_data())
        # print("self.args= ", self.args)

    def tearDown(self):
        self.args = None

    def test_repeatedNTimes(self):

        time_start = time.process_time()

        for count in range(total_loop):
            for arg in self.args:
                expected = arg.ans
                s = Solution1()
                actual = s.repeatedNTimes(arg.nums)
                self.assertEqual(expected, actual)

        time_end = time.process_time()

        print(self.__class__.__name__ + " runtime= ", time_end - time_start)


class TestSol2(unittest.TestCase):

    def setUp(self):
        self.args = (generate_data())
        # print("self.args= ", self.args)

    def tearDown(self):
        self.args = None

    def test_repeatedNTimes(self):

        time_start = time.process_time()

        for count in range(total_loop):
            for arg in self.args:
                expected = arg.ans
                s = Solution2()
                actual = s.repeatedNTimes(arg.nums)
                self.assertEqual(expected, actual)

        time_end = time.process_time()

        print(self.__class__.__name__ + " runtime= ", time_end - time_start)


if __name__ == '__main__':
    unittest.main()
