# Insertion Sort

def insertionSort1(n, arr):

    for i in range(n):
        temp = arr[i]
        j = i

        while j > 0 and arr[j-1] > temp:
            arr[j] = arr[j-1]
            print(*arr)
            j -= 1
        arr[j] = temp

    print(*arr) 
