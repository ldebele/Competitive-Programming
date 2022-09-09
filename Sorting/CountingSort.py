# Counting Sort

def countingSort(arr):
    count_array = [0 for _ in range(100)]

    for i in range(len(arr)):
        count_array[arr[i]] += 1

    z = 0
    for i in range(100):
        while count_array[i] > 0:
            arr[z] = i
            z += 1
            count_array[i] -= 1

    return arr

