class Solution:
    def nearestExit(self, maze: list[list[str]], entrance: list[int]) -> int:
        r, c = len(maze), len(maze[0])

        startR, startC = entrance
        queue = deque([(startR, startC)])
        maze[startR][startC] = '+'
        step = 0
        while queue:
            step += 1
            for i in range(len(queue)):
                currentR, currentC = queue.popleft()
                direction = [[0, -1], [0, 1], [-1, 0], [1, 0]]
                for rOff, cOff in direction:
                    nextR = currentR + rOff
                    nextC = currentC + cOff

                    if nextR >= 0 and nextR < r and nextC >= 0 and nextC < c and maze[nextR][nextC] == '.':
                        if nextR == 0 or nextR == r - 1 or nextC == 0 or nextC == c - 1:
                            return step
                        queue.append((nextR, nextC))
                        maze[nextR][nextC] = '+'
        return -1
