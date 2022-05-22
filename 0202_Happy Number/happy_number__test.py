import unittest
from dataclasses import dataclass

from happy_number import Solution1
import time

total_loop = 1000
print("total_loop= ", total_loop)


@dataclass
class TestData:
    n: None
    ans: bool


def generate_data():
    data = [TestData(19, True),
            TestData(2, False),
            ]

    return data


class TestSol1(unittest.TestCase):

    def setUp(self):
        self.args = (generate_data())
        # print("self.args= ", self.args)

    def tearDown(self):
        self.args = None

    def test_isHappy(self):

        time_start = time.process_time()

        for count in range(total_loop):
            for arg in self.args:
                expected = arg.ans
                s = Solution1()
                actual = s.isHappy(arg.n)
                self.assertEqual(expected, actual)

        time_end = time.process_time()

        print(self.__class__.__name__ + " runtime= ", time_end - time_start)


if __name__ == '__main__':
    unittest.main()
