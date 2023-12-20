"""
You are given an integer array prices representing the prices of various chocolates in a store. You are also given a single integer money, which represents your initial amount of money.

You must buy exactly two chocolates in such a way that you still have some non-negative leftover money. You would like to minimize the sum of the prices of the two chocolates you buy.

Return the amount of money you will have leftover after buying the two chocolates. If there is no way for you to buy two chocolates without ending up in debt, return money. Note that the leftover must be non-negative.


Example 2:

Input: prices = [3,2,3], money = 3
Output: 3
Explanation: You cannot buy 2 chocolates without going in debt, so we return 3.

"""

class Solution:
    def buyChoco(self, prices: list[int], money: int) -> int:
        min1 = min2 = float('inf')
        
        # find two minimum prices
        for p in prices:
            if p < min1:
                min1, min2 = p, min1
            elif p < min2:
                min2 = p
        
        # get remaining money
        leftover = money - min1 - min2
        
        return leftover if leftover >=0 else money
    
    
prices = [3,2,3]
money = 3
x = Solution()

print(x.buyChoco(prices, money))

        