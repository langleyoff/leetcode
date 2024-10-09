class Solution:
    """
    Complexity: O(n)
    Time: 39ms (Beats: 38.10%)
    Memory: 16.52MB (Beats: 48.48%)
    """
    def reverse(self, x: int) -> int:
        result = 0
        negative = x < 0

        if negative:
            x = -x

        while x != 0:
            x, rem = divmod(x, 10)
            result = result * 10 - rem if negative else result * 10 + rem

            if not (-2 ** 31 <= result <= 2 ** 31 - 1):
                return 0

        return result
