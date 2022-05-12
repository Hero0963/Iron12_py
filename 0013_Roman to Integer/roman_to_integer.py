class Solution1:
    """
    solution 1
    time complexity=O(N)
    space complexity=O(1)
    """

    def romanToInt(self, s: str) -> int:
        m = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

        lst = list(s)

        s = 0
        last = 0

        for i in range(len(lst) - 1, -1, -1):
            tmp = m[lst[i]]
            sign = 1
            if tmp < last:
                sign = -1

            s = s + (tmp * sign)
            last = tmp

        return s


class Solution2:
    """
    solution 2
    time complexity=O(N)
    space complexity=O(1)
    """

    def romanToInt(self, s: str) -> int:
        values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

        lst = list(s)
        total = 0
        last = 0

        for i in reversed(range(len(lst))):
            tmp = values[lst[i]]
            sign = 1
            if tmp < last:
                sign = -1

            total = total + (tmp * sign)
            last = tmp

        return total
