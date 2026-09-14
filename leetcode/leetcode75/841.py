class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()

        def dfs(roomIndex):
            if roomIndex in visited:
                return 
            visited.add(roomIndex)

            for k in rooms[roomIndex]:
                dfs(k)
        dfs(0)
        return len(visited) == len(rooms)
