class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        corresponding = {')': '(', '}': '{', ']': '['}

        for parenthesis in s:
            if parenthesis not in corresponding:
                stack.append(parenthesis)
            elif len(stack) == 0 or stack.pop() != corresponding[parenthesis]:
                return False
        return len(stack) == 0
