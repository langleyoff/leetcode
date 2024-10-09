class Solution:
    """
    Complexity: O(n)
    Time: 50ms (Beats: 81.38%)
    Memory: 16.70MB (Beats: 47.63%)
    """
    def lengthOfLongestSubstring(self, s: str) -> int:
        letters = set()
        left = 0
        right = 0
        max_ = 0

        while right < len(s):
            if s[right] not in letters:
                letters.add(s[right])
                right += 1
                if max_ < right - left:
                    max_ = right - left
            else:
                if max_ < right - left:
                    max_ = right - left
                letters.remove(s[left])
                left += 1

        return max_
