# solution1
class Solution1:
    """
    N=number of digits
    time: O(N)
    space: O(1)
    """

    def isHappy(self, n: int) -> bool:
        while n != 1:
            n = helper(n)
            if n < 10:
                if n == 1 or n == 7:
                    return True
                else:
                    return False

        return True


def helper(n):
    new = 0
    while n != 0:
        r = n % 10
        new += r * r
        n = n // 10

    return new
