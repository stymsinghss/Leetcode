class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest, start = 0, 0

        for i in range(len(s)):
            # for odd length string
            left, right = i, i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                cur_longest = right - left + 1
                if cur_longest > longest:
                    longest = cur_longest
                    start = left
                left-=1
                right+=1

            # for even length string
            left, right = i, i+1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                cur_longest = right - left + 1
                if cur_longest > longest:
                    longest = cur_longest
                    start = left
                left-=1
                right+=1

        substring = s[start: start+longest]
        return substring