class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        len_needle, len_haystack = len(needle), len(haystack)
        for i in range(len_haystack - len_needle + 1):
            if haystack[i: i+len_needle] == needle:
                return i
        return -1