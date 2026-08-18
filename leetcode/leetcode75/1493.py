# OG
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        countingOne = 0
        countingZero = 0
        longest = 0
        left = 0
        if 0 not in nums:
            return len(nums) - 1
        for right in range(len(nums)):
            if nums[right] == 1:
                countingOne += 1
            elif nums[right] == 0 and countingZero < 2:
                countingZero += 1
                countingOne += 1
            elif countingZero == 2:
                left = right
                countingOne = 1
            longest = max(longest, countingOne)
        return longest

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        countingOne = 0
        countingZero = 0
        longest = 0
        left = 0
        if 0 not in nums:
            return len(nums) - 1
        for right in range(len(nums)):
            if nums[right] == 0:
                countingZero += 1
            while countingZero > 1:
                if nums[left] == 0:
                    countingZero -= 1
                left += 1
            
            longest = max(longest, right - left)
        return longest
