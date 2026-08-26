# First thought
class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        left = 0
        right = 0
        counter1s = 0
        answer = s
        subStr = ""
        for right in range(len(s)):
            if s[right] == '1' and counter1s <= k:
                counter1s += 1
                subStr = s[left:right+1]
            if s[right] == '0':
                subStr = s[left:right+1]
            if counter1s > k:
                left += 1
                if s[left] == '1':
                    counter1s -= 1
                subStr = s[left:right+1]
            if len(subStr) < len(answer) and counter1s == k:
                answer = subStr
        return answer


# Solution
class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        left = 0
        right = 0
        counter1s = 0
        answer = ""
        for right in range(len(s)):
            if s[right] == '1':
                counter1s += 1
                while counter1s > k:
                    if s[left] == '1':
                        counter1s -= 1
                    left += 1
                while left <= right and s[left] == '0':
                    left += 1
                if counter1s == k:
                    current = s[left:right + 1]

                    if (answer == '' or len(answer) > len(current) or (len(answer) == len(current) and answer > current)):
                        answer = current
        return answer


# Reference
class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        cnt1 = 0 
        left = 0 
        ans = s 
        if s.count('1') < k:
            return ''

        for right, x in enumerate(s):
            if x == '1':
                cnt1 += int(x)

            while cnt1 > k or s[left] == '0':

                cnt1 -= int(s[left])
                left += 1 
            if cnt1 == k:
                 t = s[left: right + 1]
                 if len(t) < len(ans) or len(t) == len(ans) and t < ans:
                    ans = t
        return ans 
