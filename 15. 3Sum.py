from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = set()
        length = len(nums)

        for i in range(length-2):
            j, k = i+1, length-1
            while j < k:
                summed_val = nums[i] + nums[j] + nums[k]
                if summed_val == 0:
                    ans.add((nums[i], nums[j], nums[k]))
                    while j < k and nums[j] == nums[k]:
                        j+=1
                        k-=1
                    j+=1
                    k-=1
                elif summed_val > 0:
                    k-=1
                else:
                    j+=1
        return list(ans)