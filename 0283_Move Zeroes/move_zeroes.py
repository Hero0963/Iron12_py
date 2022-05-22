from typing import List


# solution1
class Solution1:
    """
    N=len(nums)
    time: O(N)
    space: O(1)
    """

    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pos = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[pos] = nums[i]
                pos += 1

        while pos < len(nums):
            nums[pos] = 0
            pos += 1


# solution2
class Solution2:
    """
    N=len(nums)
    time: O(N)
    space: O(1)
    """

    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pos = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[pos], nums[i] = nums[i], nums[pos]
                pos += 1
