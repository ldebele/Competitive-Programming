class Solution:
   
    def Fizz_buzz(self, n):
        List = []

        for i in range(1, int(n+1)):
            
            if i%3==0 and i%5==0:
                List.append("FizzBuzz")
            elif i%3==0:
                List.append("Fizz")
            elif 1%5==0:
                List.append("Buzz")
            else:
                List.append(str(i))

        return List