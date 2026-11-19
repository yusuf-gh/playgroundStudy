class Solution:
    def reverse(self, x: int) -> int:

        if x < -(2 ** 31) or x > 2 ** 31 - 1:
            return 0

        sign = -1 if x < 0 else 1  # откладка знака
        n = abs(x)  # абсолютное значение числа
        rev = 0

        while n > 0:
            digit = n % 10
            rev = rev * 10 + digit
            n //= 10
        return sign * rev



