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

# Optimized
class Solution:
    def sumGame(self, num: str) -> bool:
        half = len(num) // 2

        left_sum = right_sum = 0
        left_q = right_q = 0

        for i, ch in enumerate(num):
            if i < half:
                if ch == '?':
                    left_q += 1
                else:
                    left_sum += int(ch)
            else:
                if ch == '?':
                    right_q += 1
                else:
                    right_sum += int(ch)

        if (left_q + right_q) % 2 == 1:
            return True

        return left_sum - right_sum != (right_q - left_q) // 2 * 9

# Reference


class Solution:
    """LeetCode solution class."""

    def sumGame(self, num: str) -> bool:  # noqa: N802
        """Return whether Alice wins the digit-sum game under optimal play."""
        half = len(num) // 2
        left, right = num[:half], num[half:]

        sum_left = sum(int(c) for c in left if c != "?")
        sum_right = sum(int(c) for c in right if c != "?")
        questions_left = left.count("?")
        questions_right = right.count("?")

        if (questions_left + questions_right) % 2 != 0:
            return True

        diff = sum_left - sum_right
        return 2 * diff != 9 * (questions_right - questions_left)


