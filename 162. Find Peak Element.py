from typing import List

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        length = len(nums)

        if len(nums) == 1:
            return 0

        # Test Case -> [1,0]
        if nums[0] > nums[1]:
            return 0

        # Test Case -> [8,9]
        if nums[length - 1] > nums[length-2]:
            return length-1

        # Check for peak in the remaining elements
        low, high = 1, length-2
        while low <= high:
            mid = low + (high - low)//2
            # Case1 -> peak element
            if nums[mid] > nums[mid-1] and nums[mid] > nums[mid+1]:
                return mid
            elif nums[mid] > nums[mid-1] and nums[mid] < nums[mid+1]:
                low = mid+1
            else:
                high = mid-1
        return -1