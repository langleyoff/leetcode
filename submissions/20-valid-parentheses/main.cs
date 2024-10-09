public class Solution {
    /// <summary>
    /// Complexity: O(n)
    /// Time: 80ms (Beats: 5.84%)
    /// Memory: 37.93MB (Beats: 100.00%)
    /// </summary>
    public bool IsValid(string s) {
        var stack = new Stack<char>();
        var pairs = new Dictionary<char, char>() {
            {']', '['},
            {')', '('},
            {'}', '{'},
        };

        foreach (var letter in s) {
            if (pairs.TryGetValue(letter, out char enclosing)) {
                if (stack.Count == 0 || stack.Peek() != enclosing)
                    return false;
                stack.Pop();
            }
            else {
                stack.Push(letter);
            }
        }

        return stack.Count == 0;
    }
}