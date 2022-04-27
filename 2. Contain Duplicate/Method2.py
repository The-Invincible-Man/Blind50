# Time Complexity : O(n)
# Space Complexity : O(n) 

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        # Covert given list to set and check the length of original list and new list.
        return not len(nums) == len(set(nums))
