class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x > 9 and x % 10 == 0):
            return False

        rev_number = 0
        while x > rev_number:
            rev_number = rev_number * 10 + x % 10
            x //= 10

        return True if rev_number == x or rev_number//10 == x else False
    