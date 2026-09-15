class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        cities = len(isConnected)
        visited = [False] * cities
        counter = 0
        def dfs(index):
            visited[index] = True
            for j, isConnectedNeighbor in enumerate(isConnected[index]):
                if not visited[j] and isConnectedNeighbor:
                    dfs(j)
        for i in range(cities):
            if not visited[i]:
                dfs(i)
                counter += 1
        return counter
