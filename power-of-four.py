
class Solution:

    def isPowerOfFour(self, n):

        if n==1:
            return True

        n = n/4

        if n%4==0 and n!=0:
            self.isPowerOfFour(n)
            return True
        
        return False
         

if __name__=='__main__':
    sln = Solution()

    print(sln.isPowerOfFour(16)) # Return True
    print(sln.isPowerOfFour(5)) # Return False
    print(sln.isPowerOfFour(1)) # Return True
