class SmallestInfiniteSet:

    def __init__(self):
        self.sortedSet = SortedSet(range(1,10001))

    def popSmallest(self) -> int:
        ans = self.sortedSet[0]
        self.sortedSet.remove(ans)
        return ans

    def addBack(self, num: int) -> None:
        self.sortedSet.add(num)
