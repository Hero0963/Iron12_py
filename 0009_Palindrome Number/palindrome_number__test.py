import unittest

from dataclasses import dataclass
from palindrome_number import Solution1
from palindrome_number import Solution2
from palindrome_number import Solution3
from palindrome_number import Solution4
import time

total_loop = 1000
print("total_loop= ", total_loop)


@dataclass
class TestData:
    x: int
    ans: bool


def generate_data():
    data = [TestData(121, True),
            TestData(-121, False),
            TestData(10, False),
            TestData(6789876, True)
            ]

    return data


class TestSol1(unittest.TestCase):

    def setUp(self):
        self.args = (generate_data())
        # print("self.args= ", self.args)

    def tearDown(self):
        self.args = None

    def test_isPalindrome(self):

        time_start = time.process_time()

        for count in range(total_loop):
            for arg in self.args:
                expected = arg.ans
                s1 = Solution1()
                actual = s1.isPalindrome(arg.x, )
                self.assertEqual(expected, actual)

        time_end = time.process_time()

        print("Solution1 runtime= ", time_end - time_start)


class TestSol2(unittest.TestCase):

    def setUp(self):
        self.args = (generate_data())
        # print("self.args= ", self.args)

    def tearDown(self):
        self.args = None

    def test_isPalindrome(self):

        time_start = time.process_time()

        for count in range(total_loop):
            for arg in self.args:
                expected = arg.ans
                s2 = Solution2()
                actual = s2.isPalindrome(arg.x, )
                self.assertEqual(expected, actual)

        time_end = time.process_time()

        print("Solution2 runtime= ", time_end - time_start)


class TestSol3(unittest.TestCase):

    def setUp(self):
        self.args = (generate_data())
        # print("self.args= ", self.args)

    def tearDown(self):
        self.args = None

    def test_isPalindrome(self):

        time_start = time.process_time()

        for count in range(total_loop):
            for arg in self.args:
                expected = arg.ans
                s3 = Solution3()
                actual = s3.isPalindrome(arg.x, )
                self.assertEqual(expected, actual)

        time_end = time.process_time()

        print("Solution3 runtime= ", time_end - time_start)


class TestSol4(unittest.TestCase):

    def setUp(self):
        self.args = (generate_data())
        # print("self.args= ", self.args)

    def tearDown(self):
        self.args = None

    def test_isPalindrome(self):

        time_start = time.process_time()

        for count in range(total_loop):
            for arg in self.args:
                expected = arg.ans
                s4 = Solution4()
                actual = s4.isPalindrome(arg.x, )
                self.assertEqual(expected, actual)

        time_end = time.process_time()

        print("Solution4 runtime= ", time_end - time_start)


if __name__ == '__main__':
    unittest.main()
