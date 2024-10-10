class Solution:
    """
    Complexity: O(n)
    Time: 81ms (Beats: 90.02%)
    Memory: 21.16MB (Beats: 69.99%)
    """
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies = dict()
        buckets = [None] * (len(nums) + 1)
        result = []

        for num in nums:
            frequencies[num] = frequencies.get(num, 0) + 1

        for num, frequency in frequencies.items():
            if buckets[frequency] is None:
                buckets[frequency] = list()
            buckets[frequency].append(num)

        for i in range(len(nums), 0, -1):
            if buckets[i] is None:
                continue
            for num in buckets[i]:
                if k == 0:
                    return result
                result.append(num)
                k -= 1
        return result
