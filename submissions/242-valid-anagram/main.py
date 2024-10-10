class Solution:
    """
    Complexity: O(n)
    Time: 51ms (Beats: 45.91%)
    Memory: 17.05MB (Beats: 29.51%)
    """
    def isAnagram(self, s: str, t: str) -> bool:
        letters = dict()

        for letter in s:
            letters[letter] = letters.get(letter, 0) + 1

        for letter in t:
            if letter not in letters or letters[letter] == 0:
                return False
            letters[letter] -= 1
        return all(count == 0 for count in letters.values())
