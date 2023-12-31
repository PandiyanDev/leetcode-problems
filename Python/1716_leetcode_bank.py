""" 
Hercy wants to save money for his first car. He puts money in the Leetcode bank every day.

He starts by putting in $1 on Monday, the first day. Every day from Tuesday to Sunday, he will put in $1 more than the day before. On every subsequent Monday, he will put in $1 more than the previous Monday.
Given n, return the total amount of money he will have in the Leetcode bank at the end of the nth day.

Example 2:

Input: n = 10
Output: 37
Explanation: After the 10th day, the total is (1 + 2 + 3 + 4 + 5 + 6 + 7) + (2 + 3 + 4) = 37. Notice that on the 2nd Monday, Hercy only puts in $2.
"""

class Solution:
    def totalMoney(self, n: int) -> int:
        weeks, days , result = 0, 0, 0
        
        for i in range(1, n+1):
            days += 1
            result = result + days + weeks
            if i % 7 == 0:
                weeks += 1
                days = 0
        
        return result 
        
        
        
n = 10        
x = Solution()
print(x.totalMoney(n))