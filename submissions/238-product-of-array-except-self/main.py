class Solution:
    """
    Time complexity: O(n)
    Space complexity: O(n)
    Time: 286ms (Beats: 18.85%)
    Memory: 26.30MB (Beats: 23.75%)
    """
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # According to constraints, len(nums) >= 2
        prefixes = [nums[0]] * len(nums)
        suffixes = [nums[-1]] * len(nums)
        result = [0] * len(nums)

        for i in range(1, len(nums)):
            prefixes[i] = nums[i] * prefixes[i - 1]
        for i in range(len(nums) - 2, -1, -1):
            suffixes[i] = nums[i] * suffixes[i + 1]
        for i in range(len(nums)):
            if i == 0:
                prefix = 1
                suffix = suffixes[i + 1]
            elif i == len(nums) - 1:
                prefix = prefixes[len(nums) - 2]
                suffix = 1
            else:
                prefix = prefixes[i - 1]
                suffix = suffixes[i + 1]

            result[i] = prefix * suffix

        return result

