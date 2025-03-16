class Solution:
    def reverse(self, x: int) -> int:
        rev_num = 0
        INT_MIN, INT_MAX = -2**31, 2**31-1

        sign = True
        if x < 0:
            sign = False
            x = abs(x)

        while x > 0:
            rev_num = rev_num*10 + x%10
            if INT_MIN > rev_num > INT_MAX:
                return 0
            x //= 10

        return rev_num if sign else -1 * rev_num
