class Solution:
    def checkDivisibility(self, n: int) -> bool:
        digits = [int(d) for d in str(n)]
        sumDigits = sum(digits)
        proDigits = prod(digits)
        total = sumDigits + proDigits 
        return True if n % total == 0 else False
        # return if n % total == 0
