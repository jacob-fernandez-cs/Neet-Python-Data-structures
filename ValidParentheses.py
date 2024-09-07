class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {")" : "(", "]" : "[", "}" : "{"}

        for c in s:
            if c in closeToOpen: #if this is a closing parentheses, every key is a closing parentheses
                if stack and stack[-1] == closeToOpen[c]: #if the stack is not empty (if stack) and the top of stack(stack[-1]) is the matching opening parentheses pop
                    stack.pop()
                else:
                    return False #parentheses did not match return false
            else:
                stack.append(c) #add as many opening brackets as needed
        return True if not stack else False #return true if the stack is empty (if not stack) else return false

s = "(()[]{})"

Solution = Solution()
print(Solution.isValid(s))