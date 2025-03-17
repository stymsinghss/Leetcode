from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []

        sorted_intervals = sorted(intervals, key = lambda x:x[0])
        ans = [sorted_intervals[0]]

        for i in range(1, len(sorted_intervals)):
            prev_interval = ans[-1]
            if sorted_intervals[i][0] > prev_interval[1]:
                ans.append(sorted_intervals[i])
            else:
                # merge case
                ans[-1][1] = max(prev_interval[1], sorted_intervals[i][1])
        return ans
        