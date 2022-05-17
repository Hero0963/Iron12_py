from typing import Optional


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# solution1
class Solution1:
    """
    solution 1
    N= length of ListNode
    time complexity=O(N)
    space complexity=O(1)
    """

    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False

        slow, fast = head, head.next

        while fast is not None and fast.next is not None:
            if slow == fast:
                return True

            slow = slow.next
            fast = fast.next.next

        return False


# solution2
class Solution2:
    """
    solution 2
    N= length of ListNode
    time complexity=O(N)
    space complexity=O(1)
    """

    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast = slow = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if fast == slow:
                return True

        return False
