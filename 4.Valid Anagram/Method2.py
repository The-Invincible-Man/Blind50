
# Time Complexity : O(n)
# Space Complexity: O(26)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # intialize alphabates array with size 26 as we have 26 letter a-z.
        alphabates = [0]*26
        
        for i in s:
            # update the index for s string as +1.
            alphabates[ord(i)-ord('a')]+=1
        
        for i in t:
             # update the index for t string as -1.
            alphabates[ord(i)-ord('a')]-=1
            
        # if all values in alphabates array = 0 than return true else false.
        return alphabates.count(0) == 26
        
        
        
        
