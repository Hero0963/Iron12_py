import unittest
from dataclasses import dataclass
from typing import List

from binary_watch import Solution1
from binary_watch import Solution2
import time

total_loop = 1000
print("total_loop= ", total_loop)


@dataclass
class TestData:
    turnedOn: int
    ans: List[str]


def generate_data():
    data = [TestData(1, ["0:01", "0:02", "0:04", "0:08", "0:16", "0:32", "1:00", "2:00", "4:00", "8:00"]),
            TestData(9, []),
            ]

    return data


class TestSol1(unittest.TestCase):

    def setUp(self):
        self.args = (generate_data())
        # print("self.args= ", self.args)

    def tearDown(self):
        self.args = None

    def test_readBinaryWatch(self):

        time_start = time.process_time()

        for count in range(total_loop):
            for arg in self.args:
                expected = arg.ans
                expected.sort()
                s = Solution1()
                actual = s.readBinaryWatch(arg.turnedOn)
                actual.sort()
                self.assertEqual(expected, actual)

        time_end = time.process_time()

        print(self.__class__.__name__ + " runtime= ", time_end - time_start)


class TestSol2(unittest.TestCase):

    def setUp(self):
        self.args = (generate_data())
        # print("self.args= ", self.args)

    def tearDown(self):
        self.args = None

    def test_readBinaryWatch(self):

        time_start = time.process_time()

        for count in range(total_loop):
            for arg in self.args:
                expected = arg.ans
                expected.sort()
                s = Solution2()
                actual = s.readBinaryWatch(arg.turnedOn)
                actual.sort()
                self.assertEqual(expected, actual)

        time_end = time.process_time()

        print(self.__class__.__name__ + " runtime= ", time_end - time_start)


if __name__ == '__main__':
    unittest.main()
