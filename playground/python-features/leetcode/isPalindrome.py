class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < -(2 ** 31) or x > 2 ** 31 - 1:
            return False
        elif x < 0 and x // 10 == 0:
            return False

        n = x
        rev = 0

        while n > 0:
            digit = n % 10
            rev = rev * 10 + digit
            n //= 10

        return x == rev or x == (rev // 10)



