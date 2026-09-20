class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        def quick(l, r):
            if l == r:
                return nums[l]
            i,j = l -1, r + 1

            p = nums[(l + r) >> 1]
            while i < j:
                while True:
                    i += 1
                    if nums[i] >= p:
                        break
                while True:
                    j -= 1
                    if nums[j] <= p:
                        break
                if i < j:
                    nums[i], nums[j] = nums[j], nums[i]
            
            if j < target:
                return quick(j + 1, r)
            else:
                return quick(l, j)

        target = len(nums) - k
        return quick(0, len(nums) - 1)
