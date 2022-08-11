
class Solution:

    def smallerNumbersThanCurrent(self, nums):

        nm = []
        
        for num in nums:
            count = 0
            for i in range(len(nums)):
                if num > nums[i]:
                    count += 1
            nm.append(count)

        return nm
            

    




if __name__=='__main__':
    sln = Solution()

    num = [8, 1, 2, 2, 3]
    # sln.smallerNumbersThanCurrent(num)
    print(sln.smallerNumbersThanCurrent(num))