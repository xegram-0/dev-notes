# not entirely solveable by self
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowel = ['a', 'i', 'u', 'e', 'o', 'A', 'I', 'U', 'E', 'O']
        temp = []
        for i in range(len(s)):
            if s[i] in vowel:
                temp.append(s[i])
        reversedList = list(reversed(temp))
        
        newstr = []
        n= 0
        for i in range(len(s)):
            
            if s[i] in vowel:
                newstr.append(reversedList[n])
                n += 1
            else:
                newstr.append(s[i])
        result = ''.join(newstr)
        return result
# 2 pointer 
class Solution:
    def reverseVowels(self, s: str) -> str:
      # better way to declare list
        vowels = set("aeiouAEIOU")
        chars = list(s)

        left = 0
        right = len(chars) - 1

        while left < right:
            while left < right and chars[left] not in vowels:
                left += 1

            while left < right and chars[right] not in vowels:
                right -= 1

            chars[left], chars[right] = chars[right], chars[left]
            left += 1
            right -= 1

        return "".join(chars)
