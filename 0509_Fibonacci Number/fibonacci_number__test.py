import unittest

from dataclasses import dataclass
from fibonacci_number import Solution1
from fibonacci_number import Solution2
from fibonacci_number import Solution3

import time

total_loop = 10
print("total_loop= ", total_loop)


@dataclass
class TestData:
    n: int
    ans: int


def generate_data():
    data = [TestData(2, 1),
            TestData(3, 2),
            TestData(4, 3),
            TestData(25, 75025),
            ]

    return data


class TestSol1(unittest.TestCase):

    def setUp(self):
        self.args = (generate_data())
        # print("self.args= ", self.args)

    def tearDown(self):
        self.args = None

    def test_fib(self):

        time_start = time.process_time()

        for count in range(total_loop):
            for arg in self.args:
                expected = arg.ans
                s1 = Solution1()
                actual = s1.fib(arg.n)
                self.assertEqual(expected, actual)

        time_end = time.process_time()

        print("Solution1 runtime= ", time_end - time_start)


class TestSol2(unittest.TestCase):

    def setUp(self):
        self.args = (generate_data())
        # print("self.args= ", self.args)

    def tearDown(self):
        self.args = None

    def test_fib(self):

        time_start = time.process_time()

        for count in range(total_loop):
            for arg in self.args:
                expected = arg.ans
                s2 = Solution2()
                actual = s2.fib(arg.n)
                self.assertEqual(expected, actual)

        time_end = time.process_time()

        print("Solution2 runtime= ", time_end - time_start)


class TestSol3(unittest.TestCase):

    def setUp(self):
        self.args = (generate_data())
        # print("self.args= ", self.args)

    def tearDown(self):
        self.args = None

    def test_fib(self):

        time_start = time.process_time()

        for count in range(total_loop):
            for arg in self.args:
                expected = arg.ans
                # actual = Solution3.fib(self, arg.n)
                s3 = Solution3()
                actual = s3.fib(arg.n)
                self.assertEqual(expected, actual)

        time_end = time.process_time()

        print("Solution3 runtime= ", time_end - time_start)


if __name__ == '__main__':
    unittest.main()
