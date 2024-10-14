class Solution:
    """
    Complexity: O(n)
    Time: 43ms (Beats: 88.32%)
    Memory: 16.68MB (Beats: 48.98%)
    """
    def finalPrices(self, prices: List[int]) -> List[int]:
        next_price_map = {}
        min_stack = []

        for i, price in enumerate(prices):
            while min_stack and price <= min_stack[-1][0]:
                next_price_map[min_stack[-1][1]] = price
                min_stack.pop()

            min_stack.append((price, i))

        """
        We can do this for a bit more clarity:

        while len(min_stack) > 0:
            next_element_map[min_stack.pop()] = 0

        And then in return just access map element [..._map[i] for i ...]
        """

        return [price - next_price_map.get(i, 0) for i, price in enumerate(prices)]
