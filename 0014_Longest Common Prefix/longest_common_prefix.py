from typing import List


class Solution1:
    """
    solution 1
    N=len(strs)
    M=min length of element in strs
    time complexity=O(NM)
    space complexity=O(1)
    """

    def longestCommonPrefix(self, strs: List[str]) -> str:

        if len(strs) == 0:
            return ""

        lcp = ""
        s = len(strs[0])

        for i in range(len(strs)):
            t = len(strs[i])
            if s > t:
                s = t

        if s == 0:
            return lcp

        for i in range(s):
            for j in range(1, len(strs)):
                if strs[0][i] != strs[j][i]:
                    return lcp

            lcp += strs[0][i]

        return lcp
