from typing import List


# solution1
class Solution1:
    """
    solution 1
    N= len(nums)
    time complexity=O(N)
    space complexity=O(N)
    """

    def majorityElement(self, nums: List[int]) -> int:
        tinydict = {}
        half = len(nums) // 2

        for x in nums:
            if x not in tinydict:
                tinydict[x] = 1
            else:
                tinydict[x] += 1

            if tinydict[x] > half:
                return x

        return -1


# solution2
class Solution2:
    """
    solution 2
    N= len(nums)
    time complexity=O(N)
    space complexity=O(1)
    """

    def majorityElement(self, nums: List[int]) -> int:
        candidate = nums[0]
        count = 0

        for x in nums:
            if count == 0:
                candidate = x
                count += 1
                continue

            if candidate == x:
                count += 1
            else:
                count -= 1

        return candidate
