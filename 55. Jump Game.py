from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        length = len(nums)
        goal = length-1

        for i in range(length-2, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        return goal == 0
