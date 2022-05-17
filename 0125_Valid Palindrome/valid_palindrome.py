# solution1
class Solution1:
    """
    solution 1
    N= len(str)
    time complexity=O(N)
    space complexity=O(1)
    """
    def isPalindrome(self, s: str) -> bool:
        head = 0
        tail = len(s) - 1

        while head < tail:
            if not s[head].isalnum():
                head += 1
                continue

            if not s[tail].isalnum():
                tail -= 1
                continue

            if s[head].lower() != s[tail].lower():
                return False

            head += 1
            tail -= 1

        return True


# solution2
class Solution2:
    """
    solution 2
    N= len(str)
    time complexity=O(N)
    space complexity=O(1)
    """
    def isPalindrome(self, s: str) -> bool:
        if s == " ":
            return True

        s = "".join(filter(str.isalnum, s)).lower()
        test = s[::-1]
        if test == s:
            return True
        else:
            return False
