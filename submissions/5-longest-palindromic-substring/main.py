class Solution:
    """
    Complexity: O(n^2)
    Time: 290ms (Beats: 72.56%)
    Memory: 16.65MB (Beats: 45.21%)
    """
    def longestPalindrome(self, s: str) -> str:
        def expand(left, right) -> str:
            if right >= len(s) or left != right and s[left] != s[right]:
                return s[left]

            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]

        current = ""
        for i in range(len(s)):
            poly = expand(i, i)
            if len(poly) > len(current):
                current = poly

            poly = expand(i, i + 1)
            if len(poly) > len(current):
                current = poly

        return current
