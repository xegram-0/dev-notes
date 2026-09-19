class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        r, c = len(grid), len(grid[0])
        freshCount = 0
        q = deque()
        for rIndex in range(r):
            for cIndex in range(c):
                if grid[rIndex][cIndex] == 2:
                    q.append((rIndex, cIndex))
                elif grid[rIndex][cIndex] == 1:
                    freshCount += 1
        
        minute = 0
        direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        while q and freshCount > 0:
            minute += 1
            currentLv = len(q)
            for i in range(currentLv):
                currentR, currentC = q.popleft()
                for rDelta, cDelta in direction:
                    nextR = currentR + rDelta
                    nextC = currentC + cDelta

                    if (0 <= nextR < r and 0 <= nextC < c and grid[nextR][nextC] == 1):
                        grid[nextR][nextC] = 2
                        q.append((nextR, nextC))
                        freshCount -= 1

                        if freshCount == 0:
                            return minute
        return -1 if freshCount > 0 else 0
