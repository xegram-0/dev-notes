# My solution
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        a = nums[0]
        b = 0
        c = 0
        n = len(nums)
        if n < 3:
            return False
        for i in range(n-2):
            if nums[i] < a:
                a = nums[i]
            if nums[i+1] > a:
                b = nums[i+1]
            if nums[i+2] > a and nums[i+2] > b:
                c = nums[i+2]
            if a < b and b < c:
                return True
        return False

# Faster runtime
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        a = float('inf')
        b = float('inf')
        for num in nums:
            if num <= a:
                a = num
            elif num <= b:
                b = num
            else:
                return True
        return False
