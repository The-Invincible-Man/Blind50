# Time Complexity : O(n*n) 
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # maximum profit 
        max_profit = 0
        
        # Check for every possible pair
        for i in range (len(prices)):
            
            for j in range (i+1,len(prices)):
                
                # update maximum profit till now
                max_profit = max(max_profit,prices[j]-prices[i])
        
    
        return max_profit
