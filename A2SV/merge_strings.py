

def merge_alternately(word1, word2):

    merged = ""

    n = max(len(word1), len(word2))

    for i in range(n):

        if (i+1) <= len(word1) and (i+1) <= len(word2):
            merged = merged + word1[i] + word2[i]
        elif (i+1) > len(word1) and (i+1) <= len(word2):
            merged = merged + word2[i]
        elif (i+1) > len(word2)  and (i+1) <= len(word1):
            merged = merged + word1[i]


    return merged



if __name__ == "__main__":

    word1 = "abcd"
    word2 = "pq"

    merged_words = merge_alternately(word1, word2)
    print(merged_words)