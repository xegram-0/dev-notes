# attempt 1
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vs = ['a', 'i', 'u', 'e', 'o']
        currentV = s[:k]
        for v in currentV:
            if v not in vs:
                currentV = currentV.replace(v,"")
        maxV = len(currentV)
        for v in range(k, len(s)):
            if s[v] in vs:
                currentV -= s[v - k]
                currentV += s[v]
                maxV = max(len(currentV), len(maxV))
        return maxV

# attempt 2

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vs = ['a', 'i', 'u', 'e', 'o']
        count = 0
        windows = s[:k]
        for i in range(k, len(s)):
            if s[i] in vs:
                count += 1
                windows -= s[i - k]
                windows += s[i]
                if count > k:
                    count = 3
        return count
# solution
  class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vs = ('a', 'i', 'u', 'e', 'o')
        count = sum(1 for c in s[:k] if c in vs)
        maxCount = count
        for right in range(k, len(s)):
            if s[right] in vs:
                count += 1
            if s[right - k] in vs:
                count -= 1
            maxCount = max(count, maxCount)
        return maxCount

# faster?
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set("aeiou")
        
        count = 0
        
        # First window
        for i in range(k):
            if s[i] in vowels:
                count += 1
        
        ans = count
        
        # Slide the window
        for i in range(k, len(s)):
            if s[i] in vowels:
                count += 1
            
            if s[i - k] in vowels:
                count -= 1
            
            ans = max(ans, count)
        
        return ans
