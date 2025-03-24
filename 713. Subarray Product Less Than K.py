from typing import List

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        subarray_count = 0
        prod, left = 1, 0

        for right in range(len(nums)):
            # expand
            prod *= nums[right]

            # shrink
            while prod >= k and left <= right:
                prod //= nums[left]
                left += 1

            subarray_count += (right - left)+1
        return subarray_count
