from typing import List

# solution1
"""
time: O(n) 
space: O(1)
"""


class Solution1:
    def plusOne(self, digits: List[int]) -> List[int]:
        add = 1
        for i in range(len(digits) - 1, -1, -1):
            r = (digits[i] + add) % 10
            add = (digits[i] + add) // 10
            digits[i] = r

            if add == 0:
                break

        if add != 0:
            digits.insert(0, add)

        return digits
