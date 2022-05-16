import unittest
from dataclasses import dataclass

from plus_one import Solution1
import time

total_loop = 1000
print("total_loop= ", total_loop)


@dataclass
class TestData:
    digits: None
    ans: None


def generate_data():
    data = [TestData([1, 2, 3], [1, 2, 4]),
            TestData([4, 3, 2, 1], [4, 3, 2, 2]),
            TestData([9], [1, 0])
            ]

    return data


class TestSol1(unittest.TestCase):

    def __init__(self, methodName: str = ...):
        super().__init__(methodName)
        self.__class__name = None

    def setUp(self):
        self.args = (generate_data())
        # print("self.args= ", self.args)

    def tearDown(self):
        self.args = None

    def test_plusOne(self):

        time_start = time.process_time()

        for count in range(total_loop):

            self.setUp()

            for arg in self.args:
                expected = arg.ans
                s = Solution1()
                actual = s.plusOne(arg.digits)
                self.assertEqual(expected, actual)

            self.tearDown()

        time_end = time.process_time()

        print(self.__class__.__name__ + " runtime= ", time_end - time_start)


if __name__ == '__main__':
    unittest.main()
