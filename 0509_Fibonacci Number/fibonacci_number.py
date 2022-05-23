class Solution1:
    """
    solution 1
    time complexity=O(N)
    space complexity=O(1)
    """

    def fib(self, n: int) -> int:
        if n <= 1:
            return n

        first = 0
        second = 1
        total = 0

        for i in range(2, n + 1):
            # print("i,first,second,total= %d %d %d %d" % (i, first, second, total))
            total = first + second
            first = second
            second = total

        return total


# ref = https://www.geeksforgeeks.org/program-for-nth-fibonacci-number/


class Solution2:
    """
    solution 2
    time complexity=O(log(N))
    space complexity=O(1)
    """

    def fib(self, n: int) -> int:
        max_number = 31
        f = [0] * max_number

        # Base cases
        if n == 0:
            return 0
        if n == 1 or n == 2:
            f[n] = 1
            return f[n]

        if f[n]:
            return f[n]

        if n & 1:
            k = (n + 1) // 2
        else:
            k = n // 2

        if n & 1:
            f[n] = (self.fib(k) * self.fib(k) + self.fib(k - 1) * self.fib(k - 1))
        else:
            f[n] = (2 * self.fib(k - 1) + self.fib(k)) * self.fib(k)

        return f[n]


class Solution3:
    """
    solution 3
    time complexity=O(2^N)
    space complexity=O(1)
    """

    def fib(self, n: int) -> int:
        if n <= 1:
            return n

        return self.fib(n - 1) + self.fib(n - 2)
