from typing import List
from collections import Counter

class Solution:
    # Fixed window
    def findAnagramsFixedWindow(self, s: str, p: str) -> List[int]:
        anagrams = []

        len_p, len_s = len(p), len(s)
        counter_p = Counter(p)

        for i in range(len_s - len_p + 1):
            window = s[i:i+len_p]
            counter_window = Counter(window)
            if counter_p == counter_window:
                anagrams.append(i)

        return anagrams

    # Variable window
    def findAnagramsVariableWindow(self, s: str, p: str) -> List[int]:
        anagrams = []

        mapper = {}
        len_p, len_s = len(p), len(s)
        counter_p = Counter(p)
        left = 0

        for right in range(len_s):
            # expand the window
            mapper[s[right]] = mapper.get(s[right], 0) + 1

            # shrink the window
            if right - left + 1 > len_p:
                mapper[s[left]] -= 1
                if mapper[s[left]] == 0:
                    del mapper[s[left]]
                left += 1

            if mapper == counter_p:
                anagrams.append(left)
        return anagrams