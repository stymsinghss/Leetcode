from typing import List
from functools import cmp_to_key

class Solution:
    def custom_compare(self, first: str, second: str):
        if first + second < second + first:
            return 1
        elif first + second > second + first:
            return -1
        else:
            return 0

    def largestNumber(self, nums: List[int]) -> str:
        string_nums = map(str, nums)

        ans = sorted(string_nums, key=cmp_to_key(self.custom_compare))
        return ''.join(ans)