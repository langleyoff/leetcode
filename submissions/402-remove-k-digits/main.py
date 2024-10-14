class Solution:
    """
    Complexity: O(n)
    Time: 87ms (Beats: 15.52%)
    Memory: 20.78MB (Beats: 5.15%)
    """
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []

        for char in num:
            while stack and int(char) < stack[-1] and k != 0:
                stack.pop()
                k -= 1

            stack.append(int(char))

        while stack and k > 0:
            stack.pop()
            k -= 1

        result = "".join(map(str, stack)).lstrip("0")

        return result if result else "0"
