# solution (cannot think of it)
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        count = 0
        maxLength = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                count += 1
            while count > k:
                if nums[left] == 0:
                    count -= 1
                left += 1
            maxLength = max(maxLength, right - left + 1)
        return maxLength

expand right
count zeroes
if zeroes > k:
    shrink from left
record the valid window length
# optimized
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        zc=0
        l=0
        for i in nums:
            if i == 0:
                zc+=1
            if zc>k:
                if nums[l]==0:
                    zc-=1
                l+=1
        return len(nums)-l
