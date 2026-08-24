class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        rowDict = Counter(tuple(row) for row in grid)
        answer = 0
        for col in zip(*grid):
            answer += rowDict[col]
        return answer
