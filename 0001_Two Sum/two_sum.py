from typing import List


class Solution1:
    """
    solution 1
    time complexity=O(N)
    space complexity=O(N)
    """

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for idx, val in enumerate(nums):
            diff = target - val
            if diff in hash_map:
                return [hash_map[diff], idx]
            else:
                hash_map[val] = idx

        return [-1, -1]


# solution 2
class Solution2:
    """
    solution 2
    time complexity=O(N)
    space complexity=O(N)
    """

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = dict()
        for i in range(len(nums)):
            if target - nums[i] in hash_map:
                return [hash_map[target - nums[i]], i]
            else:
                hash_map[nums[i]] = i

        return [-1, -1]


# solution 3
class Solution3:
    """
    solution 3
    time complexity=O(N^2)
    space complexity=O(1)
    """

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

        return [-1, -1]
