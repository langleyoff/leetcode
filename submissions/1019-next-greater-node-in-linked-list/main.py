# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    """
    Complexity: O(n)
    Time: 167ms (Beats: 38.80%)
    Memory: 20.00MB (Beats: 46.63%)
    """
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        mono_decr_stack = []
        node_map = {}
        node = head
        index = 0

        while node is not None:
            node_map[index] = node
            node = node.next
            index += 1

        result = [0] * index
        node = head
        index = 0

        while node is not None:
            while mono_decr_stack and node.val > node_map[mono_decr_stack[-1]].val:
                result[mono_decr_stack.pop()] = node.val
            mono_decr_stack.append(index)
            node = node.next
            index += 1

        return result


# Other option with "convert linked list to array" coding approach
class Solution:
    """
    Complexity: O(n)
    Time: 152ms (Beats: 88.91%)
    Memory: 19.65MB (Beats: 62.17%)
    """
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        mono_decr_stack = []
        values = []

        while head is not None:
            values.append(head.val)
            head = head.next

        result = [0] * len(values)

        for i, value in enumerate(values):
            while mono_decr_stack and value > values[mono_decr_stack[-1]]:
                result[mono_decr_stack.pop()] = value
            mono_decr_stack.append(i)

        return result
