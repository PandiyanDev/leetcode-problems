"""
A peak element is an element that is strictly greater than its neighbors.

Given a 0-indexed integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.

You may imagine that nums[-1] = nums[n] = -∞. In other words, an element is always considered to be strictly greater than a neighbor that is outside the array.

You must write an algorithm that runs in O(log n) time.

Example 2:

Input: nums = [1,2,1,3,5,6,4]
Output: 5
Explanation: Your function can return either index number 1 where the peak element is 2, or index number 5 where the peak element is 6.

"""

class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        n = len(nums)
        start = 0 
        end = n -1
        if n == 1:
            return 0
        while start <= end:
            mid = start + (end - start) // 2
            if mid == 0: ## initial element of a list
                if nums[mid] > nums[mid+1]:
                    return mid
                else:
                    start = mid + 1
            elif mid == n-1:
                if nums[mid] > nums[mid -1]:
                    return mid
                else:
                    end = mid -1
            else:
                if nums[mid] > nums[mid-1] and nums[mid] > nums[mid+1]:
                    return mid
                else:
                    if nums[mid] < nums[mid+1]:
                        start = mid + 1
                    else:
                        end = mid -1
        return -1
                
                    
        
        
        
x= Solution()
print(x.findPeakElement([1,2,1,3,5,6,4])) ## output: 5