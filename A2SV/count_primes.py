
class CountPrimes():

    def count_primes(self, n):
        
        primes = [] 

        if n <= 2:
            return 0

        for i in range(2, n, 1):   
            prime = []


            for j in range(1, i, 1):

                if i % j == 0:
                    prime.append(j)
            
            if len(prime) == 1:
                primes.append(i)

        return primes


    def count_prime_number(self, n):

        if n <= 2:
            return 0 
        elif n == 3:
            return 1

        primes = [2, 3]

        i = 1

        while True:

            left = 6*i - 1
            right = 6*i + 1

            if left <= n:
                primes.append((6*i - 1))
            
            if right <= n:
                primes.append((6*i + 1))

            if left >= n or right >= n:
                break

            i += 1


        return primes
        


        
if __name__ == "__main__":
    
    # input 
    n = int(input())

    cp = CountPrimes()
    # primes = cp.count_primes(n)

    primes = cp.count_prime_number(n)
    print(primes)


