import unittest

from dataclasses import dataclass
from my_sqrt import Solution1
from my_sqrt import Solution2
from my_sqrt import Solution3
from my_sqrt import Solution4

import time

total_loop = 1000
print("total_loop= ", total_loop)


@dataclass
class TestData:
    x: int
    ans: int


def generate_data():
    data = [TestData(4, 2),
            TestData(8, 2),
            ]

    return data


class TestSol1(unittest.TestCase):

    def setUp(self):
        self.args = (generate_data())
        # print("self.args= ", self.args)

    def tearDown(self):
        self.args = None

    def test_mySqrt(self):

        time_start = time.process_time()

        for count in range(total_loop):
            for arg in self.args:
                expected = arg.ans
                s1 = Solution1()
                actual = s1.mySqrt(arg.x)
                self.assertEqual(expected, actual)

        time_end = time.process_time()

        print("Solution1 runtime= ", time_end - time_start)


class TestSol2(unittest.TestCase):

    def setUp(self):
        self.args = (generate_data())
        # print("self.args= ", self.args)

    def tearDown(self):
        self.args = None

    def test_mySqrt(self):

        time_start = time.process_time()

        for count in range(total_loop):
            for arg in self.args:
                expected = arg.ans
                s2 = Solution2()
                actual = s2.mySqrt(arg.x)
                self.assertEqual(expected, actual)

        time_end = time.process_time()

        print("Solution2 runtime= ", time_end - time_start)


class TestSol3(unittest.TestCase):

    def setUp(self):
        self.args = (generate_data())
        # print("self.args= ", self.args)

    def tearDown(self):
        self.args = None

    def test_mySqrt(self):

        time_start = time.process_time()

        for count in range(total_loop):
            for arg in self.args:
                expected = arg.ans
                s3 = Solution3()
                actual = s3.mySqrt(arg.x)
                self.assertEqual(expected, actual)

        time_end = time.process_time()

        print("Solution3 runtime= ", time_end - time_start)


class TestSol4(unittest.TestCase):

    def setUp(self):
        self.args = (generate_data())
        # print("self.args= ", self.args)

    def tearDown(self):
        self.args = None

    def test_mySqrt(self):

        time_start = time.process_time()

        for count in range(total_loop):
            for arg in self.args:
                expected = arg.ans
                s4 = Solution4()
                actual = s4.mySqrt(arg.x)
                self.assertEqual(expected, actual)

        time_end = time.process_time()

        print("Solution4 runtime= ", time_end - time_start)


if __name__ == '__main__':
    unittest.main()
