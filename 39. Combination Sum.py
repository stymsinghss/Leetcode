from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        combs = []
        self.generate(candidates, target, combs, [], 0)
        return combs

    def generate(self, nums, target, combs, temp, idx):
        if target == 0:
            combs.append(temp[:])
            return

        if target < 0:
            return

        for i in range(idx, len(nums)):
            temp.append(nums[i])
            self.generate(nums, target - nums[i], combs, temp, i)
            temp.pop()
            