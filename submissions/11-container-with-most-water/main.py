class Solution:
    """
    Complexity: O(n)
    Time: 452ms (Beats: 98.19%)
    Memory: 30.14MB (Beats: 7.84%)
    """
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_ = -1

        while left < right:
            if height[left] < height[right]:
                if height[left] * (right - left) > max_:
                    max_ = height[left] * (right - left)
                left += 1
            else:
                if height[right] * (right - left) > max_:
                    max_ = height[right] * (right - left)
                right -= 1

        return max_
