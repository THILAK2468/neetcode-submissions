class Solution:
    def isValid(self, s: str) -> bool:
        pran = {'}':'{',']':'[',')':'('}
        stack = []

        for char in s:
            if char in pran:
                if stack and stack[-1] == pran[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        return not stack