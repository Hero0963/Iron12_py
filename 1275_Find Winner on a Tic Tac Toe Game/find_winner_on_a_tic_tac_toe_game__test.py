import unittest
from dataclasses import dataclass
from typing import List

from find_winner_on_a_tic_tac_toe_game import Solution1
import time

total_loop = 1000
print("total_loop= ", total_loop)


@dataclass
class TestData:
    moves: List[List[int]]
    ans: str


def generate_data():
    data = [TestData([[0, 0], [2, 0], [1, 1], [2, 1], [2, 2]], "A"),
            TestData([[0, 0], [1, 1], [0, 1], [0, 2], [1, 0], [2, 0]], "B"),
            TestData([[0, 0], [1, 1], [2, 0], [1, 0], [1, 2], [2, 1], [0, 1], [0, 2], [2, 2]], "Draw"),
            ]

    return data


class TestSol1(unittest.TestCase):

    def setUp(self):
        self.args = (generate_data())
        # print("self.args= ", self.args)

    def tearDown(self):
        self.args = None

    def test_tictactoe(self):

        time_start = time.process_time()

        for count in range(total_loop):
            for arg in self.args:
                expected = arg.ans
                s = Solution1()
                actual = s.tictactoe(arg.moves)
                self.assertEqual(expected, actual)

        time_end = time.process_time()

        print(self.__class__.__name__ + " runtime= ", time_end - time_start)


if __name__ == '__main__':
    unittest.main()
