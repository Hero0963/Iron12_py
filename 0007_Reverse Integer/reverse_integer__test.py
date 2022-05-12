import unittest

from dataclasses import dataclass
from reverse_integer import Solution1
from reverse_integer import Solution2
import time

total_loop = 1000
print("total_loop= ", total_loop)


@dataclass
class TestData:
    x: int
    ans: int


def generate_data():
    data = [TestData(123, 321),
            TestData(-123, -321),
            TestData(120, 21),
            TestData(6789876, 6789876)
            ]

    return data


class TestSol1(unittest.TestCase):

    def setUp(self):
        self.args = (generate_data())
        # print("self.args= ", self.args)

    def tearDown(self):
        self.args = None

    def test_reverse(self):

        time_start = time.process_time()

        for count in range(total_loop):
            for arg in self.args:
                expected = arg.ans
                s1 = Solution1()
                actual = s1.reverse(arg.x)
                self.assertEqual(expected, actual)

        time_end = time.process_time()

        print("Solution1 runtime= ", time_end - time_start)


class TestSol2(unittest.TestCase):

    def setUp(self):
        self.args = (generate_data())
        # print("self.args= ", self.args)

    def tearDown(self):
        self.args = None

    def test_reverse(self):

        time_start = time.process_time()

        for count in range(total_loop):
            for arg in self.args:
                expected = arg.ans
                s2 = Solution2()
                actual = s2.reverse(arg.x)
                self.assertEqual(expected, actual)

        time_end = time.process_time()

        print("Solution2 runtime= ", time_end - time_start)


if __name__ == '__main__':
    unittest.main()
