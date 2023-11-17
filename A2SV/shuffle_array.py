

class ShuffleArray():

    def shuffle_array(self, nums, n):

        shuffled_nums = [] 

        for i in range(n):
            shuffled_nums.append(nums[i])
            shuffled_nums.append(nums[i+n])

        return shuffled_nums


if __name__ == "__main__":

    # nums = [2, 5, 1, 3, 4, 7]
    # n = 3

    # nums = [1, 2, 3, 4, 4, 3, 2, 1]
    # n = 4

    nums = [1, 1, 2, 2]
    n = 2

    shuffle = ShuffleArray()
    shuffled = shuffle.shuffle_array(nums, n)

    print(shuffled)
