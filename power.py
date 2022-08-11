
class Solution:
    def myPow(self, x, n):
        if n>=0:
            if n==0:
                return 1
            else:
                if n%2==0:
                    return self.myPow(x*x, n//2)
                else:
                    return x * self.myPow(x*x, n//2)
        else:
            x = 1/x
            n = abs(n)
            return self.myPow(x, n)
            
     


if __name__ == '__main__':
    sln = Solution()

    print(sln.myPow(2.00000, 10)) # return 1024
    print(sln.myPow(2.0, -2)) # return 0.25
    print(sln.myPow(2.10, 3)) # return 9.2610