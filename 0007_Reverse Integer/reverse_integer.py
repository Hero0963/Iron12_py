class Solution1:
    """
    solution 1
    x: bounded
    time complexity=O(1)
    space complexity=O(1)
    """

    def reverse(self, x: int) -> int:

        upper_bound = (1 << 31) - 1
        lower_bound = -1 << 31

        sign = 1
        if x < 0:
            sign = -1
            x = -x

        lst = list(str(x))
        lst.reverse()

        r = ""

        if sign < 1:
            r = "-"

        str_rev_x = "".join(lst)
        r += str_rev_x

        y = int(r)

        if y > upper_bound or y < lower_bound:
            return 0

        return y


class Solution2:
    """
    solution 2
    x: bounded
    time complexity=O(1)
    space complexity=O(1)
    """

    def reverse(self, x: int) -> int:

        upper_bound = (1 << 31) - 1
        lower_bound = -1 << 31

        prey = 0
        y = 0
        r = 0
        fix = 0
        sign = 1
        if x < 0:
            sign = -1
            x = -x

        # print("x= ", x)

        while x > 0:
            r = x % 10
            y = y * 10 + r

            fix = int((y - r) / 10)

            if fix != prey:
                return 0

            prey = int(y)
            x = int(x / 10)

        y = y * sign

        if y > upper_bound or y < lower_bound:
            return 0

        return y
