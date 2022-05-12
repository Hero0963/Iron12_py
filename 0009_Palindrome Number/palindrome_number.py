import copy


class Solution1:
    """
    solution 1
    x: unbounded
    time complexity=O(N)
    space complexity=O(N)
    """

    def isPalindrome(self, x: int) -> bool:

        if x < 0:
            return False

        if x == 0:
            return True

        lst = list(str(x))
        lst2 = copy.deepcopy(lst)
        lst2.reverse()

        # print("lst= ", lst)
        # print("lst2= ", lst2)

        if lst == lst2:
            return True

        return False


class Solution2:
    """
    solution 2
    x: unbounded
    time complexity=O(N)
    space complexity=O(N)
    """

    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        if x == 0:
            return True

        lst = []
        y = 0
        r = 0

        while x > 0:
            r = x % 10
            lst.append(r)
            x = int(x / 10)

        head = 0
        tail = len(lst) - 1

        while head < tail:
            if lst[head] != lst[tail]:
                return False

            head += 1
            tail -= 1

        return True


class Solution3:
    """
    solution 3
    x: unbounded
    time complexity=O(N)
    space complexity=O(1)
    """

    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        if x == 0:
            return True

        if x % 10 == 0:
            return False

        rev = 0
        r = 0

        while rev < x:
            r = x % 10
            rev = rev * 10 + r
            x = int(x / 10)

        # print("x= ", x)
        # print("rev= ", rev)

        if (x == rev) or (x == int(rev / 10)):
            return True

        return False


class Solution4:
    """
    solution 4
    x: unbounded
    time complexity=O(N)
    space complexity=O(N)
    """

    def isPalindrome(self, x: int) -> bool:
        str1 = str(x)
        str2 = str(x)[::-1]
        return str1 == str2
