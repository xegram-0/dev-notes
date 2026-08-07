# My solution:
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candies = max(candies)
        boolList = []
        for i, candy in enumerate(candies):
            if ((candies[i] + extraCandies) >= max_candies):
                boolList.append(True)
            else:
                boolList.append(False)
        return boolList
# Perfect form:
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candies = max(candies)
        return [candy + extraCandies >= max_candies for candy in candies]
