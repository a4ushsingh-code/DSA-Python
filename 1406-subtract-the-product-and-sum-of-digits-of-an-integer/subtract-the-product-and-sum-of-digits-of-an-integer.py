class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product = 1
        sum = 0
        while n > 0:
            last_digit = n%10
            product = product*last_digit
            sum = sum+last_digit
            n = n//10
        return product-sum
        