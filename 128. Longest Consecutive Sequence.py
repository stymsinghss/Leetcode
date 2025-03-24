from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        nums = set(nums)
        for num in nums:
            if num - 1 not in nums:
                # start of the sequence
                length = 0
                while num + length in nums:
                    length += 1
                longest = max(longest, length)
        return longest