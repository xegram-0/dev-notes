class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True
        for i in range(len(flowerbed)):
            leftplot = (i == 0 or flowerbed[i-1] == 0)
            rightplot = ( i == len(flowerbed) -1 or flowerbed[i+1] == 0)
            if flowerbed[i] == 0 and leftplot and rightplot:
                flowerbed[i] = 1
                n -= 1
            if n == 0:
                return True
        return False


# Slightly better
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True
        for i in range(len(flowerbed)):
            if (
                flowerbed[i] == 0
                and (i == 0 or flowerbed[i - 1] == 0)
                and (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0)
            ):
                flowerbed[i] = 1
                n -= 1

                if n == 0:
                    return True

        return False
