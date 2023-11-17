

def is_palindrome(x):

    x = str(x)

    if x == x[::-1]:
        return True
    else:
        return False


if __name__ == "__main__":

    x = -121

    n = is_palindrome(x)
    print(n)