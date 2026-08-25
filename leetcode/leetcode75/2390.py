# First thought
class Solution:
    def removeStars(self, s: str) -> str:
        newS = ""
        for i in range(len(s)):
            if s[i] != '*':
                newS += s[i]
            else:
                newS = newS.replace(s[i - 1], '')
        return newS


# Solution
class Solution:
    def removeStars(self, s: str) -> str:
        temp = []
        for c in s:
            if c != '*':
                temp.append(c)
            else:
                temp.pop()
        return ''.join(temp)


# Reference 
class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for ch in s:
            if ch == "*":
                stack.pop()
            else:
                stack.append(ch)
        return "".join(stack)
