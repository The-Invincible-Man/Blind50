class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # we are running the nested loop to check every possible pair.
        # Time Complexity : o(n*n)
        # Space Complexity : o(1)
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j] == target:
                    return [i,j]
