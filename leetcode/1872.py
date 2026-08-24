class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        prefix = stones[:]

        for i in range(1, len(prefix)):
            prefix[i] += prefix[i - 1]

        best = prefix[-1]

        for i in range(len(stones) - 2, 0, -1):
            best = max(best, prefix[i] - best)

        return best
