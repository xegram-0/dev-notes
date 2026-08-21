class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count = {}
        for num in arr:
            count[num] = count.get(num,0) + 1
        values = list(count.values())
        if len(values) != len(set(values)):
            return False
        else:
            return True


# Better version
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count = {}

        for num in arr:
            count[num] = count.get(num, 0) + 1

        values = list(count.values())

        return len(values) == len(set(values))
