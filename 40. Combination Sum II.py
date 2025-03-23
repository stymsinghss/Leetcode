from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        combs = set()
        self.generate(candidates, target, combs, [], 0)
        return list(combs)

    def generate(self, nums, target, combs, temp, idx):
        if target == 0:
            combs.add(tuple(temp[:]))
            return

        if target < 0:
            return

        for i in range(idx, len(nums)):
            if i > idx and nums[i] == nums[i-1]:
                continue
            temp.append(nums[i])
            self.generate(nums, target - nums[i], combs, temp, i+1)
            temp.pop()
            