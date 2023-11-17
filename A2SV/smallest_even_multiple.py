

"""
    2 | 15
2   1 | 15
15  1 | 1
"""


def smallest_even_multiple(n):
     
    if n % 2 == 0 :
        return n
    else:
        return n * 2


if __name__ == "__main__":

    n = 8

    SEM = smallest_even_multiple(n)
    print(SEM)





