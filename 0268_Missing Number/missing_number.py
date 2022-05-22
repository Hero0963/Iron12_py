from typing import List


# solution1
class Solution1:
    """
    N=len(nums)
    time: O(N)
    space: O(1)
    """

    def missingNumber(self, nums: List[int]) -> int:
        l = len(nums)
        r = l

        for i in range(l):
            r = r + i - nums[i]

        return r


# solution2
class Solution2:
    """
    N=len(nums)
    time: O(N)
    space: O(1)
    """

    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        s = sum(nums)

        r = (n * (n + 1)) // 2 - s

        return r


# solution3
class Solution3:
    """
    N=len(nums)
    time: O(N)
    space: O(1)
    """

    def missingNumber(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)

        for i in range(1, n + 1):
            ans ^= i ^ nums[i - 1]

        return ans
