
class Solution:

    def fibonacci(self, n):

        if n==0:
            return 0

        elif n==1:
            return 1

        else:
            return self.fibonacci(int(n-1)) + self.fibonacci(int(n-2))


if __name__=='__main__':
    sln = Solution()

    print(sln.fibonacci(8))