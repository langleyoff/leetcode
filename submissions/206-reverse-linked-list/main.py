class Solution:
    """
    Complexity: O(n)
    Time: 25ms (Beats: 98.48%)
    Memory: 17.59MB (Beats: 98.96%)
    """
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None

        current = ListNode(head.val, None)
        head = head.next

        while head is not None:
            next_ = head.next
            head.next = current
            current = head
            head = next_

        return current
