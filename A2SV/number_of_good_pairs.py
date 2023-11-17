

from tokenize import Number


class NumberOfGoodPairs():

    def num_identical_pairs(self, nums):

        identical_pairs = []

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):

                if nums[i] == nums[j]:
                    identical_pairs.append((i, j))

        return len(identical_pairs)


if __name__ == "__main__":
    
    # nums = input()
    # nums = [1, 2, 3, 1, 1, 3]
    nums = [1, 1, 1, 1]
    nums = [1, 2, 3]

    nip = NumberOfGoodPairs()
    ip = nip.num_identical_pairs(nums)
    print(ip)