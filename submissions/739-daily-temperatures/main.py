class Solution:
    """
    Complexity: O(n)
    Time: 867ms (Beats: 88.24%)
    Memory: 30.87MB (Beats: 75.03%)
    """
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        mono_decr_stack = []
        result = [0] * len(temperatures)

        for index, temperature in enumerate(temperatures):
            while mono_decr_stack and temperatures[mono_decr_stack[-1]] < temperature:
                prev_index = mono_decr_stack.pop()
                result[prev_index] = index - prev_index
            mono_decr_stack.append(index)

        return result
