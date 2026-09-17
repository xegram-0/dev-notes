class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        def find(node):
            if parent[node] != node:
                ogParent = parent[node]
                parent[node] = find(parent[node])
                weight[node] *= weight[ogParent]
            return parent[node]
        
        weight = defaultdict(lambda: 1.0)
        parent = defaultdict(str)

        for num, denom in equations:
            parent[num] = num
            parent[denom] = denom
        
        for i, value in enumerate(values):
            num, denom = equations[i]
            rNum = find(num)
            rDenom = find(denom)

            if rNum == rDenom:
                continue
            
            parent[rNum] = rDenom
            
            weight[rNum] = weight[denom] * value / weight[num]
        
        ans = []

        for dividend, divisor in queries:
            if (dividend not in parent or divisor not in parent or find(dividend) != find(divisor)):
                ans.append(-1.0)
            else:
                ans.append(weight[dividend] / weight[divisor])
        return ans
