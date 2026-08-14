# my vision
result = 0
        for num in nums:
            otherHalf = k - num
            if otherHalf in nums:
                result += 1
        return result // 2

# hashmap
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        seen = {}
        result = 0

        for num in nums:
            complement = k - num

            if seen.get(complement, 0) > 0:
                result += 1
                seen[complement] -= 1
            else:
                seen[num] = seen.get(num, 0) + 1

        return result

# pointer 
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()

        left = 0
        right = len(nums) - 1
        result = 0

        while left < right:
            total = nums[left] + nums[right]

            if total == k:
                result += 1
                left += 1
                right -= 1
            elif total < k:
                left += 1
            else:
                right -= 1

        return result

# ??
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        total, c = 0, 0

        cnt = Counter(nums)
        

        for i in cnt:
            c += min(cnt[i], cnt[k-i])
        
        total = c//2



        return total
