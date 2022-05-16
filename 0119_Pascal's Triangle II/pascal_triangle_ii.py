from typing import List


# solution 1
class Solution1:
    """
        solution 1
        N= rowIndex
        time complexity=O(N^2)
        space complexity=O(N)
     """

    def getRow(self, rowIndex: int) -> List[int]:
        ans = [1]
        if rowIndex == 0:
            return ans

        for i in range(rowIndex):
            ans.append(1)
            for j in range(len(ans) - 2, 0, -1):
                ans[j] += ans[j - 1]

            # print("i,ans= ", i, ans)
        return ans


# solution 2
class Solution2:
    """
        solution 2
        N= rowIndex
        time complexity=O(N^2)
        space complexity=O(N)
     """

    def getRow(self, rowIndex: int) -> List[int]:
        ans = [1]
        if rowIndex == 0:
            return ans

        for i in range(rowIndex):
            ans.append(1)

            half = len(ans) // 2
            for j in range(len(ans) - 2, half - 1, -1):
                # print("j,ans,len(ans)= ", j, ans, len(ans))
                ans[j] += ans[j - 1]

            for k in range(1, half):
                ans[k] = ans[len(ans) - 1 - k]

            # print("i,ans= ", i, ans)

        return ans
