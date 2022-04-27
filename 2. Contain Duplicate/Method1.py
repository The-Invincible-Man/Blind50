# Time Complexity : O(n)
# Space Complexity: O(n)

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        # Create Emplty set
        arr = set()
        
        for val in nums :
            
            # Check if val present in arr
            if val in arr :
                
                # if present return true
                return True
            # if not present add current values in set arr.
            arr.add(val)
        
        # if no repeating value found return false
        return False
        
