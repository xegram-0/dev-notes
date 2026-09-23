class Solution:
    def totalCost(self, costs: list[int], k: int, candidates: int) -> int:
        if candidates * 2 >= len(costs):
            return sum(sorted(costs)[:k])
        h = []
        for i, cost in enumerate(costs[:candidates]):
            heappush(h, (cost, i))
        for i in range(len(costs) - candidates, len(costs)):
            heappush(h, (costs[i], i))
        leftP = candidates
        rightP = len(costs) - candidates - 1
        
        ans = 0
        for i in range(k):
            wCost, wIndex = heappop(h)
            ans += wCost
            if leftP > rightP:
                continue
            if wIndex < leftP:
                heappush(h, (costs[leftP], leftP))
                leftP += 1
            else:
                heappush(h, (costs[rightP], rightP))
                rightP -= 1
        return ans
