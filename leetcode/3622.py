class Solution:
    def checkDivisibility(self, n: int) -> bool:
        digits = [int(d) for d in str(n)]
        sumDigits = sum(digits)
        proDigits = prod(digits)
        total = sumDigits + proDigits 
        return True if n % total == 0 else False
        # return if n % total == 0

# Reference
class Solution:
    def checkDivisibility(self, n: int) -> bool:
        x = n
        digit_sum = 0
        digit_product = 1

        while x > 0:
            digit = x % 10
            digit_sum += digit
            digit_product *= digit
            x //= 10
        total = digit_sum + digit_product
        return n % total == 0
