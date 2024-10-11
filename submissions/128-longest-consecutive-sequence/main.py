class Solution:
    """
    Complexity: O(n)
    Time: 347ms (Beats: 70.43%)
    Memory: 31.86MB (Beats: 42.01%)
    """
    def longestConsecutive(self, nums: List[int]) -> int:
        elements = set(nums)
        starts = set()
        max_length = 0

        for element in elements:
            if element - 1 not in elements:
                starts.add(element)

        for start in starts:
            cur_length = 1
            cur_value = start

            while cur_value + 1 in elements:
                cur_length += 1
                cur_value += 1

            if cur_length > max_length:
                max_length = cur_length

            max_length = max(max_length, cur_length)

        return max_length
