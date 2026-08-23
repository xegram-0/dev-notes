# My solution
class Solution:
    def sumGame(self, num: str) -> bool:
        mid = len(num) // 2
        leftSum = 0
        rightSum = 0
        leftQuestion = 0
        rightQuestion = 0
        for char in num[:mid]:
            if char == '?':
                leftQuestion += 1
            else:
                leftSum += int(char)
        for char in num[mid:]:
            if char == '?':
                rightQuestion += 1
            else:
                rightSum += int(char)
        if (leftQuestion + rightQuestion) % 2 == 1:
            return True
        return leftSum - rightSum != (rightQuestion - leftQuestion) // 2 * 9
