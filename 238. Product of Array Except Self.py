from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        prefix, postfix = [0]*length, [0]*length
        prefix[0], postfix[length-1] = 1, 1

        for i in range(1, length):
            prefix[i] = nums[i-1]*prefix[i-1]
        for j in range(length-2, -1, -1):
            postfix[j] = nums[j+1] * postfix[j+1]

        print("prefix - ", prefix)
        print("postfix - ", postfix)

        for i in range(length):
            nums[i] = prefix[i]*postfix[i]
        return nums