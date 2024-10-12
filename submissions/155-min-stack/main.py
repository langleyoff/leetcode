class MinStack:
    """
    Complexity: O(1)
    Time: 51ms (Beats: 76.22%)
    Memory: 20.49MB (Beats: 86.59%)
    """
    def __init__(self):
        self._min_stack = []
        self._stack = []

    def push(self, val: int) -> None:
        self._stack.append(val)

        if len(self._min_stack) == 0 or self.getMin() >= val:
            self._min_stack.append(val)

    def pop(self) -> None:
        value = self._stack.pop()

        if self.getMin() == value:
            self._min_stack.pop()

    def top(self) -> int:
        return self._stack[-1]

    def getMin(self) -> int:
        return self._min_stack[-1]
