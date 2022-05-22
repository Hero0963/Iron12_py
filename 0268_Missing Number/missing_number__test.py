import unittest
from dataclasses import dataclass
from typing import List

from missing_number import Solution1
from missing_number import Solution2
from missing_number import Solution3
import time

total_loop = 1000
print("total_loop= ", total_loop)


@dataclass
class TestData:
    nums: List[int]
    ans: int


def generate_data():
    data = [TestData([3, 0, 1], 2),
            TestData([0, 1], 2),
            TestData([9, 6, 4, 2, 3, 5, 7, 0, 1], 8),
            ]

    return data


class TestSol1(unittest.TestCase):

    def setUp(self):
        self.args = (generate_data())
        # print("self.args= ", self.args)

    def tearDown(self):
        self.args = None

    def test_missingNumber(self):

        time_start = time.process_time()

        for count in range(total_loop):
            for arg in self.args:
                expected = arg.ans
                s = Solution1()
                actual = s.missingNumber(arg.nums)
                self.assertEqual(expected, actual)

        time_end = time.process_time()

        print(self.__class__.__name__ + " runtime= ", time_end - time_start)


class TestSol2(unittest.TestCase):

    def setUp(self):
        self.args = (generate_data())
        # print("self.args= ", self.args)

    def tearDown(self):
        self.args = None

    def test_missingNumber(self):

        time_start = time.process_time()

        for count in range(total_loop):
            for arg in self.args:
                expected = arg.ans
                s = Solution2()
                actual = s.missingNumber(arg.nums)
                self.assertEqual(expected, actual)

        time_end = time.process_time()

        print(self.__class__.__name__ + " runtime= ", time_end - time_start)


class TestSol3(unittest.TestCase):

    def setUp(self):
        self.args = (generate_data())
        # print("self.args= ", self.args)

    def tearDown(self):
        self.args = None

    def test_missingNumber(self):

        time_start = time.process_time()

        for count in range(total_loop):
            for arg in self.args:
                expected = arg.ans
                s = Solution3()
                actual = s.missingNumber(arg.nums)
                self.assertEqual(expected, actual)

        time_end = time.process_time()

        print(self.__class__.__name__ + " runtime= ", time_end - time_start)


if __name__ == '__main__':
    unittest.main()
