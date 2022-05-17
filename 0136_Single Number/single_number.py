from typing import List


# solution1
class Solution1:
    """
    solution 1
    N= len(nums)
    time complexity=O(N)
    space complexity=O(1)
    """

    def singleNumber(self, nums: List[int]) -> int:
        flag = 0
        for i in range(len(nums)):
            flag ^= nums[i]

        return flag


# solution2
class Solution2:
    """
    solution 2
    N= len(nums)
    time complexity=O(N)
    space complexity=O(1)
    """

    def singleNumber(self, nums: List[int]) -> int:
        flag = 0
        for _, val in enumerate(nums):
            flag ^= val
        return flag


# solution3
class Solution3:
    """
    solution 3
    N= len(nums)
    time complexity=O(N)
    space complexity=O(N)
    """

    def singleNumber(self, nums: List[int]) -> int:
        dict1 = {}

        for _, val in enumerate(nums):
            if val in dict1:
                del dict1[val]
            else:
                dict1[val] = 1

        for key in dict1:
            sn = key

        return sn
