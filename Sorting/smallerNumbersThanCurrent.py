
class Solution:
    def __init__(self, nums):
        self.nums = nums
        self.smaller_no = [0 for i in range(len(nums))]
        
    def smallerNumbersThanCurrent(self):
        for i in range(len(self.nums)):
            for j in range(len(self.nums)):
                if self.nums[i] > self.nums[j]:
                    self.smaller_no[i] += 1
        
        return self.smaller_no



if __name__ == "__main__":
    # nums = [8, 1, 2, 2, 3] # return [4, 0, 1, 1, 3]
    # nums = [6, 5, 4, 8] # return [2, 1, 0, 3]
    nums = [7, 7, 7, 7]  # return [0, 0, 0, 0]
    sln = Solution(nums)

    print(sln.smallerNumbersThanCurrent())
