class Solution1:
    """
    solution 1
    time complexity=O(N^0.5)
    space complexity=O(1)
    """

    def mySqrt(self, x: int) -> int:
        i = 0

        while (i * i) <= x:
            i += 1

        return i - 1


class Solution2:
    """
    solution 2
    time complexity=O(log(N))
    space complexity=O(1)
    """

    def mySqrt(self, x: int) -> int:
        if x <= 1:
            return x

        head = 0
        tail = (x // 2) + 1

        while head < tail:
            mid = head + ((tail - head) // 2)

            if mid * mid == x:
                return mid
            elif mid * mid > x:
                tail = mid
            else:
                head = mid + 1

        return tail - 1


class Solution3:
    def mySqrt(self, x: int) -> int:
        if x <= 1:
            return x

        r = x

        while r * r > x:
            r = (r + x // r) // 2

        return r


class Solution4:
    def mySqrt(self, x: int) -> int:
        return int(x ** 0.5)
