class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        
        adjacency = [[] for i in range(n)]
        for fromCity, toCity in connections:
            adjacency[fromCity].append((toCity, 1))
            adjacency[toCity].append((fromCity,0))
        def count(current, parent):
            total = 0
            for neighbor, reversal in adjacency[current]:
                if neighbor != parent:
                    total += reversal + count(neighbor, current) 
            return total   
        return count(0, -1)
