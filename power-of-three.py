
class Solution:
    def isPowerOfThree(self, n):
        n = n/3
        if n%3 == 0 and n != 0:
            self.isPowerOfThree(n)
            return True
        
        return False


if __name__=='__main__':
    sln = Solution()

    print(sln.isPowerOfThree(81))
    print(sln.isPowerOfThree(0))
    print(sln.isPowerOfThree(27))
    print(sln.isPowerOfThree(15))
