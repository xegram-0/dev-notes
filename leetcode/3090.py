# Attempt
class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        charCounter = Counter()
        ans = 0
        left = 0
        for right, c in enumerate(s):
            charCounter[c] += 1
            while charCounter[c] > 2:
                charCounter[s[left]] -= 1
                left += 1
            ans = max(ans, right - left + 1)
        return ans
# Reference
class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        l,r = 0,0
        a=collections.defaultdict(int)
        longest = 0
        while r<len(s):
            if a[s[r]] < 2:
                a[s[r]] += 1
                r+=1
                longest = max(longest,r-l)
            else:
                a[s[r]] += 1
                while a[s[r]] > 2:
                    a[s[l]]-=1
                    l+=1
                longest = max(longest,r-l)
                r+=1
        return longest

        
