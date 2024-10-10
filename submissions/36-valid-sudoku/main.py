class Solution:
    """
    Complexity: O(1)
    Space complexity: O(1)
    Time: 82ms (Beats: 95.29%)
    Memory: 16.60MB (Beats: 58.81%)
    """
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        squares = [[set() for _ in range(3)] for _ in range(3)]

        for row in range(9):
            for col in range(9):
                value = board[row][col]

                if value == '.':
                    continue

                if value in rows[row] or value in cols[col]:
                    return False
                if value in squares[row // 3][col // 3]:
                    return False

                rows[row].add(value)
                cols[col].add(value)
                squares[row // 3][col // 3].add(value)

        return True
