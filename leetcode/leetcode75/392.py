class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        y = 0
        result = ""
        while y < len(t):
            if i < len(s) and s[i] == t[y]  :
                i += 1
                result += t[y]

            y += 1

        if result == s:
            return True
        return False

  class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0

        for char in t:
            if i < len(s) and s[i] == char:
                i += 1

        return i == len(s)
