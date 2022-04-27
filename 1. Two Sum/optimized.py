# Time Complexity : O(n)
# Space Complexity : O(n)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # Initilized dictionary which store number as key and index list as value
        indexDictionary = dict()
        
        # Add index list as values and number as key 
        # Ex: ar = [1,2,2,4,5]
        # indexDictionary = {1:[0],2:[1,2],4:[3],5:[4]}
        for i in range ( len(nums) ):
            if nums[i] in indexDictionary:
                indexDictionary[nums[i]].append(i)
            else:
                indexDictionary[nums[i]] = [i]
        
        
        for i in range ( len(nums) ):
            # check if target-nums[i] in indexDictionary
            # For ex: if target = 9  nums[i] = 3
            # than if 9-3 is present in array we got the answer.
            # Python dictionatory in operation takes o(1) time.
            if target-nums[i] in indexDictionary:
                
                for ind in indexDictionary[target-nums[i]]:
                    
                    # Ex: ar = [3,3] target = 6
                    # indexDictionary = {3:[0,1]}
                    # when we search 6-3 it will again give 3 so we make sure both 3 are present on different index.
                    if ind != i:
                        return [i,ind]
                
                
        
        
        
        
