from typing import List


class Solution1:
    """
    solution 1
    N=map_size=3 ( fixed here )
    time complexity=O(N*N) or O(1) (if fixed)
    space complexity=O(N)
    """

    def tictactoe(self, moves: List[List[int]]) -> str:
        self.map_size = 3

        if len(moves) < (self.map_size - 1) ** 2:
            return "Pending"

        chess_board = [["" for y in range(len(moves))]
                       for x in range(len(moves))]

        action_A = "X"
        action_B = "O"

        for i in range(len(moves)):
            x = moves[i][0]
            y = moves[i][1]

            if i % 2 == 0:
                chess_board[x][y] = action_A
            else:
                chess_board[x][y] = action_B

        self.chess_board = chess_board

        if self.check_win(action_A):
            return "A"
        if self.check_win(action_B):
            return "B"

        if len(moves) < self.map_size ** 2:
            return "Pending"

        return "Draw"

    def check_win(self, action: str) -> bool:
        if self.check_row(action) or self.check_col(action) or self.check_diag(action):
            return True

        return False

    def check_row(self, action: str) -> bool:
        for i in range(self.map_size):
            count = 0
            for j in range(self.map_size):
                if self.chess_board[i][j] != action:
                    break
                else:
                    count += 1
            if count == self.map_size:
                return True

        return False

    def check_col(self, action: str) -> bool:
        for j in range(self.map_size):
            count = 0
            for i in range(self.map_size):
                if self.chess_board[i][j] != action:
                    break
                else:
                    count += 1
            if count == self.map_size:
                return True

        return False

    def check_diag(self, action: str) -> bool:
        count_main_diag = 0
        for i in range(self.map_size):
            if self.chess_board[i][i] != action:
                break
            else:
                count_main_diag += 1
        if count_main_diag == self.map_size:
            return True

        count_sub_diag = 0
        for j in range(self.map_size):
            if self.chess_board[j][(self.map_size - 1) - j] != action:
                break
            else:
                count_sub_diag += 1
        if count_sub_diag == self.map_size:
            return True

        return False
