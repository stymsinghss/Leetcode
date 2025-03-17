class Solution:
    # from itertools import zip_longest
    # def mergeAlternately(self, word1: str, word2: str) -> str:
    #     output = ""
    #     for c1, c2 in zip_longest(word1, word2, fillvalue=""):
    #         output += c1 if c1 != "" else c1
    #         output += c2 if c2 != "" else c2
    #
    #     return output

    def mergeAlternately(self, word1: str, word2: str) -> str:
        output = ""
        start1, start2 = 0, 0

        while start1 < len(word1) and start2 < len(word2):
            output += word1[start1]
            output += word2[start2]

            start1 += 1
            start2 += 1

        if start1 < len(word1):
            output += word1[start1: ]

        if start2 < len(word2):
            output += word2[start2: ]
        return output
