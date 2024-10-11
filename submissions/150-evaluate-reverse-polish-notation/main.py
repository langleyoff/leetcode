from math import floor, ceil


class Solution:
    """
    Complexity: O(n)
    Time: 61ms (Beats: 80.97%)
    Memory: 17.08MB (Beats: 69.11%)
    """
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token.replace('-', '').isnumeric():
                stack.append(int(token))
                continue

            right = stack.pop()
            left = stack.pop()

            if token == '+':
                value = left + right
            elif token == '-':
                value = left - right
            elif token == '*':
                value = left * right
            else:
                value = left / right
                value = floor(value) if value > 0 else ceil(value)

            stack.append(value)

        return stack.pop()
