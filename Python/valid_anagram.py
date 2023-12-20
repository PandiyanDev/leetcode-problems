""" 
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Input: s = "rat", t = "car"
Output: false
 
Input: s = "anagram", t = "nagaram"
Output: true

"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = sorted(s)
        t = sorted(t)

        if s == t:
            return True
        return False
    
    
s = "anagram", 
t = "nagaram"
x = Solution()
print(x.isAnagram(s, t))