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
# Math way
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # Add padding of 0s at both ends to handle edge cases uniformly
        # This eliminates the need for special boundary checks
        flowerbed = [0] + flowerbed + [0]
      
        # Iterate through the original flowerbed positions (excluding padding)
        for i in range(1, len(flowerbed) - 1):
            # Check if current position and both adjacent positions are empty
            # sum([left, current, right]) == 0 means all three positions are empty
            if sum(flowerbed[i - 1 : i + 2]) == 0:
                # Plant a flower at the current position
                flowerbed[i] = 1
                # Decrement the number of flowers we still need to plant
                n -= 1
      
        # Return True if we've planted all required flowers (n <= 0)
        return n <= 0
