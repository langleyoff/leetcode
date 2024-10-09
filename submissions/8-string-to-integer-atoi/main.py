class Solution:
    """
    Complexity: O(n)
    Time: 42ms (Beats: 29.77%)
    Memory: 25.63% (Beats: 25.63%)
    """
    def myAtoi(self, s: str) -> int:
        i = 0
        result = 0
        negative = False

        while i < len(s) and s[i] == ' ':
            i += 1

        if i < len(s) and s[i] == '+':
            i += 1
        elif i < len(s) and s[i] == '-':
            negative = True
            i += 1

        while i < len(s) and s[i].isnumeric():
            result = result * 10 + int(s[i])
            i += 1

        result = -result if negative else result

        if result < -2 ** 31:
            result = -2 ** 31
        elif result > 2 ** 31 - 1:
            result = 2 ** 31 - 1

        return result
