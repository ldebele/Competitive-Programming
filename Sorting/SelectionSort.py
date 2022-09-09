# Selection Sort

class Solution:
    def select(self, arr, i):
        self.selectionSort(i, len(i))

    def selectionSort(self, arr, n):
        for i in range(n-1):

            index = i
            for j in range(i, n):
                # Find the smallest item
                if arr[index] > arr[j]:
                    index = j

            if index != i:
                arr[i], arr[index] = arr[index], arr[i]

                
