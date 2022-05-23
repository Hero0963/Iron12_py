from typing import List


class Solution1:
    """
    solution 1
    time complexity=O(log(N))
    space complexity=O(1)
    """

    def search(self, nums: List[int], target: int) -> int:
        head = 0
        tail = len(nums) - 1

        while head <= tail:
            mid = head + ((tail - head) // 2)

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                tail = mid - 1
            else:
                head = mid + 1

        return -1


class Solution2:
    """
    solution 2
    time complexity=O(log(N))
    space complexity=O(1)
    """

    def search(self, nums: List[int], target: int) -> int:
        head = 0
        tail = len(nums)

        while head < tail:
            mid = head + ((tail - head) // 2)

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                tail = mid
            else:
                head = mid + 1

        return -1
