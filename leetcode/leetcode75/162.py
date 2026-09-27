class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        l, r = 0, len(nums) - 1
        index = -1
        while l <= r:
            mid = (l + r) // 2
            if mid == len(nums) - 1 or nums[mid] > nums[mid + 1]:
                index = mid
                r = mid - 1
            else:
                l = mid + 1
        return index
