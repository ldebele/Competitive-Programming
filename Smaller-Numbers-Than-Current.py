
class Solution:
    def smallerNumbersThanCurrent(self, nums):
        
        count_num = []

        for num in nums:
            count = 0
            for i in range(len(nums)):
                if num > nums[i]:
                    count += 1
            count_num.append(count)

        return count_num



if __name__=='__main__':

    sln = Solution()
    num = [8, 1, 2, 2, 3]

    print(sln.smallerNumbersThanCurrent(num))