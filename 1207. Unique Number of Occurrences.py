from collections import Counter
from typing import List

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counter = Counter(arr)
        sorted_vals = sorted(counter.items(), key = lambda x:x[1])
        for i in range(1, len(sorted_vals)):
            if sorted_vals[i][1] == sorted_vals[i-1][1]:
                return False
        return True
