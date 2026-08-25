# Dumb thought
class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        prefix = [x * k for x in nums]
        minNum = min(prefix)
        for num in prefix:
            if num not in nums:
                minNum = min(minNum, num)
        return minNum


class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        maxNum = max(nums) * k
        
        for x in range (1, maxNum + 2):
            if (x * k) not in nums:
                return x * k


# Reference
class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        s = set(nums)
        i = 1
        while True:
            if i*k not in s: return i*k
            else: i += 1
