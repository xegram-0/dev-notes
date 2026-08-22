class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        for c in word1:
            if c not in word2:
                return False
        if sorted(Counter(word1).values()) == sorted(Counter(word2).values()):
            return True
        return False

# First check
if set(word1) != set(word2):
    return False

# Optimized
from collections import Counter

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False

        c1 = Counter(word1)
        c2 = Counter(word2)

        return (
            c1.keys() == c2.keys()
            and sorted(c1.values()) == sorted(c2.values())
        )

# Top answer
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        len1=len(word1)
        len2=len(word2)
        if len1!=len2:
            return False
        num_map1=[]
        num_map2=[]
        for i in range(97, 123):
            if chr(i) in word1 and chr(i) in word2:
                num_map1.append(word1.count(chr(i)))
                num_map2.append(word2.count(chr(i)))
            elif (chr(i) in word1 and chr(i) not in word2) or (chr(i) not in word1 and chr(i) in word2):
                return False
        num_map1.sort()
        num_map2.sort()
        if num_map2==num_map1:
            return True
        return False
