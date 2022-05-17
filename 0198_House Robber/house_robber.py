from typing import List


# solution1
class Solution1:
    """
    solution 1
    N= len(nums)
    time complexity=O(N)
    space complexity=O(1)
    """

    def rob(self, nums: List[int]) -> int:
        pre2 = pre1 = 0

        for _, val in enumerate(nums):
            now = max(pre2 + val, pre1)
            pre2 = pre1
            pre1 = now

        return now
