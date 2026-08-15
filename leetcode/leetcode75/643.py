class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        currentWindow = sum(nums[:k])
        maxWindow = currentWindow

        for right in range(k, len(nums)):
            currentWindow -= nums[right - k]
            currentWindow += nums[right]
            maxWindow = max(maxWindow, currentWindow)
        result = maxWindow / k
        return result

# Better performance
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window_sum = sum(nums[:k])
        max_sum = window_sum

        for i in range(k, len(nums)):
            incoming = nums[i]
            outgoing = nums[i-k]
            window_sum = window_sum - outgoing + incoming
            if window_sum > max_sum:
                max_sum = window_sum 
        
        return max_sum/k
