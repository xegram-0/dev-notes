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
# Solution
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        resultList = [1] * n

        leftProduct = 1
        for i in range(n):
            resultList[i] = leftProduct
            leftProduct *= nums[i]

        rightProduct = 1
        for i in range(n - 1, -1 ,-1):
            resultList[i] *= rightProduct
            rightProduct *= nums[i]
        return resultList          
        
