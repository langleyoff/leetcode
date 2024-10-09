from collections import defaultdict


class Solution:
    """
    Complexity: O(n^2)
    Time: 502ms (Beats: 98.11%)
    Memory: 21.45MB (Beats: 10.22%)
    """
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # O(n*log n)
        positions = defaultdict(list)

        for i, value in enumerate(nums):
            positions[value].append(i)

        triplets = []
        prev_i = None

        for i, value in enumerate(nums):
            if prev_i == value:
                continue

            prev_i = value
            prev_j = None

            for j in range(i + 1, len(nums)):
                if prev_j == nums[j]:
                    continue
                prev_j = nums[j]

                if value + nums[j] > 0:
                    break

                target = -value - nums[j]

                if target in positions:
                    if any(x > j for x in positions[target]):
                        triplets.append([value, nums[j], target])
        return triplets
