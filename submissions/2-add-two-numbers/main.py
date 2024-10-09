class Solution:
    """
    Complexity: O(n)
    Time: 54ms (Beats: 60.64%)
    Memory: 16.58MB (Beats: 80.46%)
    """
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode()
        current = result

        while l1 is not None or l2 is not None:
            left = l1.val if l1 is not None else 0
            right = l2.val if l2 is not None else 0

            remainder, current.val = divmod(left + right + current.val, 10)

            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next

            if (l2 is not None or l1 is not None) or remainder != 0:
                current.next = ListNode(remainder)
                current = current.next

        return result