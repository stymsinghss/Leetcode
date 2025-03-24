from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        if len(nums) == 2:
            return max(nums[0], nums[1])

        amount = [0]*len(nums)
        amount[0], amount[1] = nums[0], max(nums[0], nums[1])

        for i in range(2, len(nums)):
            amount[i] = max(amount[i-1], nums[i] + amount[i-2])

        return amount[len(nums)-1]