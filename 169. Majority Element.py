from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate, votes = 0, 0

        for num in nums:
            if votes == 0:
                candidate = num
                votes = 1
            else:
                if num == candidate:
                    votes += 1
                else:
                    votes -= 1

        # validate candidate
        return candidate if nums.count(candidate) > len(nums) // 2 else -1
        