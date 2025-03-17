from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longest_common_prefix = ""

        if not strs:
            return longest_common_prefix

        sorted_strs = sorted(strs, key = len)
        smallest_string = sorted_strs[0]


        for i in range(len(smallest_string)):
            character = smallest_string[i]
            for j in range(1, len(sorted_strs)):
                if sorted_strs[j][i] != character:
                    return longest_common_prefix
            longest_common_prefix += character
        return longest_common_prefix
        