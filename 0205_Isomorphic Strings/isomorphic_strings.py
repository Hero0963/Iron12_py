# solution1
class Solution1:
    """
    N=len(s)
    M=len(t)
    time: O(N+M)
    space: O(N+M)
    """

    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(t) != len(s) or len(set(s)) != len(set(t)):
            return False

        hash_map = {}
        for char in range(len(t)):
            if t[char] not in hash_map:
                hash_map[t[char]] = s[char]
            elif hash_map[t[char]] != s[char]:
                return False
        return True


# solution2
class Solution2:
    """
    N=len(s)
    M=len(t)
    time: O(N+M)
    space: O(N+M)
    """

    def isIsomorphic(self, s: str, t: str) -> bool:
        return len(set(zip(s, t))) == len(set(s)) == len(set(t))
