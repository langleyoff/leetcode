class Solution:
    """
    Complexity: O(n)
    Time: 38ms (Beats: 54.30%)
    Memory: 16.56MB (Beats: 76.53%)
    """
    def longestCommonPrefix(self, strs: List[str]) -> str:
        max_index = min(map(lambda x: len(x), strs))
        index = 0
        prefix = ""

        if len(strs) == 1:
            return strs[0]

        while index < max_index and all(x[index] == strs[0][index] for x in strs[1::]):
            prefix += strs[0][index]
            index += 1

        return prefix
