# 1st attempt
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        tempList = []
        tempNum = 0
        product = 1
        for i in range(len(nums)):
            tempNum = nums.pop(i)
            for y in range(len(nums)):
                product *= nums[y]
            tempList.append(product)
            product = 1
            nums.insert(i, tempNum)
        return tempList
