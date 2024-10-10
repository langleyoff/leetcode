class Solution:
    """
    Complexity: O(n)
    Time: 419ms (Beats: 60.37%)
    Memory: 32.01MB (Beats: 25.53%)
    """
    def containsDuplicate(self, nums: List[int]) -> bool:
        occurrences = set()

        for num in nums:
            if num in occurrences:
                return True
            occurrences.add(num)
        return False
