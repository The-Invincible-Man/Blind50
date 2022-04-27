
# Time Complexity : O(nlog(n))
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # sort both the string and check the equality
        return sorted(s) == sorted(t)
        
