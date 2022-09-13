# Color sorting using insertion sort
class Solution:
    def sortColors(self, nums):
        for i in range(len(nums)):
            j = i
            while j > 0 and nums[j-1] > nums[j]:
                nums[j-1], nums[j] = nums[j], nums[j-1]

                j -= 1
