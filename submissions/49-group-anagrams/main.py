class Solution:
    """
    Complexity: O(n * log n)
    Time: 80ms (Beats: 92.19%)
    Memory: 20.28MB (Beats: 53.60%)
    """
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for anagram in strs:
            sorted_anagram = ''.join(sorted(anagram))

            if sorted_anagram not in groups:
                groups[sorted_anagram] = list()
            groups[sorted_anagram].append(anagram)

        return groups.values()
