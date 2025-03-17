class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s)-1

        while left <= right:
            left_char, right_char = s[left].lower(), s[right].lower()
            if left_char.isalnum() and right_char.isalnum():
                if left_char == right_char:
                    left += 1
                    right -= 1
                else:
                    return False
            elif not left_char.isalnum():
                left += 1
            elif not right_char.isalnum():
                right -= 1

        return True
