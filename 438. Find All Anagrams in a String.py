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