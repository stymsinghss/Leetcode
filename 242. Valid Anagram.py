class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False

        anagrams = [0]*26
        for i in range(len(s)):
            anagrams[ord(s[i]) - ord("a")] += 1
            anagrams[ord(t[i]) - ord("a")] -= 1

        for i in range(26):
            if anagrams[i] != 0:
                return False
        return True