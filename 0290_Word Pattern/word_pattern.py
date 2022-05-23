# solution1
class Solution1:
    """
    N=len(pattern)
    M=len(s)
    time: O(N+M)
    space: O(N)
    """

    def wordPattern(self, pattern: str, s: str) -> bool:
        str2 = s.split(' ')

        # print("pattern= ", pattern)
        # print("str2= ", str2)

        if len(pattern) != len(str2):
            # print("len(pattern)= %d,len(str2)= %d" % (len(pattern), len(str2)))
            return False

        dict1 = {}
        dict2 = {}

        for i in range(len(pattern)):
            pp, ss = pattern[i], str2[i]

            if pp not in dict1 and ss not in dict2:
                dict1[pp] = ss
                dict2[ss] = pp

            if dict1.get(pp, -1) != ss or dict2.get(ss, -2) != pp:
                # print("dict1= ", dict1)
                # print("dict2= ", dict2)
                return False

        return True


# solution2
class Solution2:
    """
    N=len(pattern)=len(s)
    time: O(N)
    space: O(N)
    """

    def wordPattern(self, pattern: str, s: str) -> bool:
        str2 = s.split(' ')

        # print("pattern= ", pattern)
        # print("str2= ", str2)

        if len(pattern) != len(str2):
            # print("len(pattern)= %d,len(str2)= %d" % (len(pattern), len(str2)))
            return False

        dict1 = {}
        dict2 = {}

        for pp, ss in zip(pattern, str2):

            if pp not in dict1 and ss not in dict2:
                dict1[pp] = ss
                dict2[ss] = pp

            if dict1.get(pp, -1) != ss or dict2.get(ss, -2) != pp:
                # print("dict1= ", dict1)
                # print("dict2= ", dict2)
                return False

        return True
