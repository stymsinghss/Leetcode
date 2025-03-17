from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapper = dict()
        for idx, val in enumerate(nums):
            to_find = target - val
            if to_find in mapper:
                return [idx, mapper[to_find]]
            mapper[val] = idx
            