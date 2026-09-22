class Solution:
    def maxScore(self, nums1: list[int], nums2: list[int], k: int) -> int:
        pair = sorted(zip(nums2,nums1), reverse=True)
        h = []
        maxScore = 0
        currentSum = 0
        for n2, n1 in pair:
            currentSum += n1
            heapq.heappush(h, n1)
            if len(h) == k:
                maxScore = max(maxScore, currentSum * n2)
                currentSum -= heapq.heappop(h)
        return maxScore
