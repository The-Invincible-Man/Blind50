# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def isValid(self, s: str) -> bool:
        
        # key value pair 
        brackets = {'(':')','{':'}','[':']'}
        
        # empty stack
        stack = []
        
        # loop over values in s
        for val in s:
            
            # val belongs to ['(','[','{'] than push data into stack
            if val in ['(','[','{']:
                stack.append(val)
            else:
                # check if stack is not emplty and if we have right close bracket pop the top element of stack.
                if stack and val == brackets[stack[-1]]:
                    stack.pop(-1)
                else:
                    return False
        # if stack is not emplty return false
        if stack:
            return False
        return True
        
