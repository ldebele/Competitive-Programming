

class SelfDividingNumbers():

    def self_dividing_numbers(self, left, right):

        output = []

    
        for num in range(left, right+1):

            self_num = []

            for i in str(num):

                if (int(i) != 0) and (num % int(i) == 0):
                    self_num.append(True)

            if len(self_num) == len(str(num)):
                output.append(num)

        return output


          
            
  




if __name__ == "__main__":

    left = int(input())
    right = int(input())

    sdn = SelfDividingNumbers()
    sdn.self_dividing_numbers(left, right)
