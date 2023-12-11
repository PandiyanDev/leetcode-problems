"""
    Given an integer array sorted in non-decreasing order, there is exactly one integer in the array that occurs more than 25% of the time, return that integer.


Example 1:

Input: arr = [1,2,2,6,6,6,6,7,10]
Output: 6
"""

    
class Solution:
    def findSpecialInteger(self, arr: list[int]) -> int:
        counts = {}
        
        for num in arr:
            if num in counts:
                counts[num] +=1
            else:
                counts[num] =1

        highest_element = None
        highest_count = 0
        
        for num, count in counts.items():
            if count > highest_count:
                highest_element = num
                highest_count = count
        
        return highest_element
    
    
arr = [1,2,2,6,6,6,6,7,10] 
x = Solution()
print(x.findSpecialInteger(arr))




        