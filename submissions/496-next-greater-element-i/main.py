class Solution:
    """
    Complexity: O(n + m)
    Time: 49ms (Beats: 54.46%)
    Memory: 16.77MB (Beats: 76.49%)
    """
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        next_element_map = {}
        min_stack = []

        for num in nums2:
            while len(min_stack) != 0 and num > min_stack[-1]:
                next_element_map[min_stack.pop()] = num

            min_stack.append(num)

        """
        We can do this for a bit more clarity:

        while len(min_stack) > 0:
            next_element_map[min_stack.pop()] = -1

        And then in return just access map element [..._map[num] for num ...]
        """

        return [next_element_map.get(num, -1) for num in nums1]
