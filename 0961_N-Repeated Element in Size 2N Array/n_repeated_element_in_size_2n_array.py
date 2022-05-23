from typing import List


class Solution1:
    """
    solution 1
    N=len(nums)
    time complexity=O((N))
    space complexity=O(N)
    """

    def repeatedNTimes(self, nums: List[int]) -> int:
        tinydict = {}

        for x in nums:
            if x not in tinydict:
                tinydict[x] = True
            else:
                return x

        return -1


class Solution2:
    """
    solution 2
    N=len(nums)
    time complexity=O((N))
    space complexity=O(1)
    """

    def repeatedNTimes(self, nums: List[int]) -> int:
        for i in range(2, len(nums)):
            if nums[i] == nums[i - 1] or nums[i] == nums[i - 2]:
                return nums[i]

        return nums[0]
