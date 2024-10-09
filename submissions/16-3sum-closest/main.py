from math import inf


class Solution:
    """
    Complexity: O(n^2)
    Time: 403ms (Beats: 62.10%)
    Memory: 16.5MB (Beats: 81.49%)
    """
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        if len(nums) == 3:
            return sum(nums)

        nums.sort()  # O(n*log n)
        result = inf

        # O(n^2)
        for i, value in enumerate(nums[0:-2]):
            left = i + 1
            right = len(nums) - 1

            while left < right:
                current = value + nums[left] + nums[right]

                if current == target:
                    return target
                if abs(current - target) < abs(result - target):
                    result = current

                if current < target:
                    left += 1
                else:
                    right -= 1
        return result
