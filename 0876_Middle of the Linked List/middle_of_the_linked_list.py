from typing import Optional


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution1:
    """
    solution 1
    N=number of nodes
    time complexity=O(N)
    space complexity=O(1)
    """

    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = slow = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow


class Solution2:
    """
    solution 2
    N=number of nodes
    time complexity=O(N)
    space complexity=O(1)
    """

    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count = 0
        current = head
        while current is not None:
            count = count + 1
            current = current.next

        middle = count // 2
        current = head

        for _ in range(middle):
            current = current.next

        return current
