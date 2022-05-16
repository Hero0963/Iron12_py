# solution 1
class Solution1:
    """
       solution 1
       time complexity=O(N)
       space complexity=O(1)
    """

    def climbStairs(self, n: int) -> int:

        if n <= 2:
            return n

        first = 1
        second = 2
        total = 0
        start = 3

        while start <= n:
            total = first + second
            first = second
            second = total
            start += 1

        return total


# solution 2
class Solution2:
    """
       solution 2
       time complexity=O(N)
       space complexity=O(1)
    """

    def climbStairs(self, n: int) -> int:

        if n <= 2:
            return n

        first = 1
        second = 2
        total = 0

        for i in range(3, n + 1):
            total = first + second
            first = second
            second = total

        return total
