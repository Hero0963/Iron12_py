# solution1
class Solution1:
    """
    N=num
    time: O(N^0.5)
    space: O(1)
    """

    def checkPerfectNumber(self, num: int) -> bool:
        if num <= 1:
            return False

        sum = 1
        i = 2
        while i * i < num:
            if num % i == 0:
                sum += i
                tmp = num // i

                if tmp != i:
                    sum += tmp

                if sum > num:
                    return False

            i += 1

        if sum != num:
            return False

        return True
