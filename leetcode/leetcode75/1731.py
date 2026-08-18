class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        altitude = [0]
        for i in range(len(gain)):
            altitude.append(altitude[-1] + gain[i]) # -1 means last element and it is updated every loop
        return max(altitude)
