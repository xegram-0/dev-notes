class Solution:
    def successfulPairs(self, spells: list[int], potions: list[int], success: int) -> list[int]:
        potions.sort()
        result = []
        for spell in spells:
            minPotion = success / spell
            insertPotion = bisect_left(potions, minPotion)
            count = len(potions) - insertPotion
            result.append(count)
        return result
