import unittest

from dataclasses import dataclass
from two_sum import Solution1
from two_sum import Solution2
from two_sum import Solution3
import time

total_loop = 1000
print("total_loop= ", total_loop)


@dataclass
class TestData:
    nums: None
    target: int
    ans: None


def generate_data():
    data = [TestData([2, 7, 11, 15], 9, [0, 1]),
            TestData([3, 2, 4], 6, [1, 2]),
            TestData([3, 3], 6, [0, 1])
            ]

    return data


class TestSol1(unittest.TestCase):

    def setUp(self):
        self.args = (generate_data())
        # print("self.args= ", self.args)

    def tearDown(self):
        self.args = None

    def test_twoSum(self):

        time_start = time.process_time()

        for count in range(total_loop):
            for arg in self.args:
                expected = arg.ans
                s1 = Solution1()
                actual = s1.twoSum(arg.nums, arg.target)
                self.assertEqual(expected, actual)

        time_end = time.process_time()

        print("Solution1 runtime= ", time_end - time_start)


class TestSol2(unittest.TestCase):

    def setUp(self):
        self.args = (generate_data())

    def tearDown(self):
        self.args = None

    def test_twoSum(self):

        time_start = time.process_time()

        for count in range(total_loop):
            for arg in self.args:
                expected = arg.ans
                s2 = Solution2()
                actual = s2.twoSum(arg.nums, arg.target)
                self.assertEqual(expected, actual)

        time_end = time.process_time()

        print("Solution2 runtime= ", time_end - time_start)


class TestSol3(unittest.TestCase):

    def setUp(self):
        self.args = (generate_data())

    def tearDown(self):
        self.args = None

    def test_twoSum(self):

        time_start = time.process_time()

        for count in range(total_loop):
            for arg in self.args:
                expected = arg.ans
                s3 = Solution3()
                actual = s3.twoSum(arg.nums, arg.target)
                self.assertEqual(expected, actual)

        time_end = time.process_time()

        print("Solution3 runtime= ", time_end - time_start)


if __name__ == '__main__':
    unittest.main()
