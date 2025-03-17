from itertools import zip_longest


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        output = ""
        for c1, c2 in zip_longest(word1, word2, fillvalue=""):
            output += c1 if c1 != "" else c1
            output += c2 if c2 != "" else c2

        return output
