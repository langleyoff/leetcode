import itertools


class Solution:
    """
    Complexity: O(n)
    Time: 56ms (Beats: 35.73%)
    Memory: 16.74MB (Beats: 35.65%)
    """
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows == len(s):
            return s

        matrix = [[] for _ in range(numRows)]
        downward = True
        pos = 0
        mpos = 0

        while pos < len(s):
            matrix[mpos].append(s[pos])

            if mpos == 0:
                downward = True
            if mpos == numRows - 1:
                downward = False
            mpos += 1 if downward else - 1
            pos += 1

        return "".join(itertools.chain(*matrix))
