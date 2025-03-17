class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True

        if not t:
            return False
        idx = 0

        for i in range(len(t)):
            if idx < len(s) and t[i] == s[idx]:
                idx += 1

            if idx == len(s):
                return True

        return False