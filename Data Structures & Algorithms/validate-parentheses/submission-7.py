class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) <=1: return False
        stack = []
        pairMap = {"(": ")", "[": "]", "{": "}"}

        for char in s:
            if char in pairMap:
                stack.append(char)
                continue
            if len(stack) > 0:
                if not pairMap[stack[-1]] == char:
                    return False
                else:
                    stack.pop()
            else:
                return False
        return True if not stack else False

        #if the char is the opener, if its a closer then if they match....if they match we need to pop

        