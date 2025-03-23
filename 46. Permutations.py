from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = []
        self.generate(nums, permutations, [])
        return permutations

    def generate(self, nums: List[int], perms: List[int], temp: List[int]) -> None:
        if len(temp) == len(nums):
            perms.append(temp[:])
            return

        for i in range(len(nums)):
            if nums[i] in temp:
                continue
            temp.append(nums[i])
            self.generate(nums, perms, temp)
            temp.pop()
