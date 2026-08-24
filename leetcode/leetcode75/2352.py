class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        rowDict = Counter(tuple(row) for row in grid)
        answer = 0
        for col in zip(*grid):
            answer += rowDict[col]
        return answer

# Reference
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        map = {}

        for row in grid:
            row_tuple = tuple(row)
            if row_tuple in map:
                map[row_tuple] += 1
            else:
                map[row_tuple] = 1
        
        pairs = 0
        for col in zip(*grid):
            if col in map:
                pairs += map[col]


        return pairs
