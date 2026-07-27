from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        closeToOpen = {')': '(', '}': '{', ']': '['}

        for c in s:
            if c in closeToOpen:
                if len(stack) != 0 and closeToOpen[c] == stack[-1]:
                    stack.pop()
                else: 
                    return False
            else:
                stack.append(c)
        
        return True if len(stack) == 0 else False 

        