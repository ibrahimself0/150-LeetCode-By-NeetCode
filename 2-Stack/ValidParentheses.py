class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for bracket in s:
            isOpen = bracket in ["[", "(", "{"]
            
            if not stack and not isOpen:
                return False
                
            if isOpen:
                stack.append(bracket)
            else:
                if not stack:
                    return False
                
                top = stack.pop()
                if (top == "[" and bracket != "]") or \
                   (top == "(" and bracket != ")") or \
                   (top == "{" and bracket != "}"):
                    return False
                    
        return not stack