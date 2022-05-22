import unittest
from dataclasses import dataclass

from isomorphic_strings import Solution1
from isomorphic_strings import Solution2
import time

total_loop = 1000
print("total_loop= ", total_loop)


@dataclass
class TestData:
    s: str
    t: str
    ans: bool


def generate_data():
    data = [TestData("egg", "add", True),
            TestData("foo", "bar", False),
            TestData("paper", "title", True),
            ]

    return data


class TestSol1(unittest.TestCase):

    def setUp(self):
        self.args = (generate_data())
        # print("self.args= ", self.args)

    def tearDown(self):
        self.args = None

    def test_isIsomorphic(self):

        time_start = time.process_time()

        for count in range(total_loop):
            for arg in self.args:
                expected = arg.ans
                s = Solution1()
                actual = s.isIsomorphic(arg.s, arg.t)
                self.assertEqual(expected, actual)

        time_end = time.process_time()

        print(self.__class__.__name__ + " runtime= ", time_end - time_start)


class TestSol2(unittest.TestCase):

    def setUp(self):
        self.args = (generate_data())
        # print("self.args= ", self.args)

    def tearDown(self):
        self.args = None

    def test_isIsomorphic(self):

        time_start = time.process_time()

        for count in range(total_loop):
            for arg in self.args:
                expected = arg.ans
                s = Solution2()
                actual = s.isIsomorphic(arg.s, arg.t)
                self.assertEqual(expected, actual)

        time_end = time.process_time()

        print(self.__class__.__name__ + " runtime= ", time_end - time_start)


if __name__ == '__main__':
    unittest.main()
