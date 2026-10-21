class Solution:
    def reverse(self, x: int) -> int:
        original = abs(x)
        rev = 0
        while original > 0:
            last_digit = original%10
            rev = rev*10+last_digit
            original = original//10

        if x < 0:
            rev = -rev

        if rev < -(2**31) or rev > (2**31 - 1):
            return 0

        return rev

        return rev
        