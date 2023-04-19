from nltk.corpus import words
import time

str = input("please enter the word: ")

time_start = time.time()


def editDistDP(str1, str2, m, n):
    dp = [[0 for x in range(n + 1)] for x in range(m + 1)]

    for i in range(m + 1):
        for j in range(n + 1):

            if i == 0:
                dp[i][j] = j

            elif j == 0:
                dp[i][j] = i

            elif str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]

            else:
                dp[i][j] = 1 + min(dp[i][j - 1],  # Insert
                                   dp[i - 1][j],  # Remove
                                   dp[i - 1][j - 1])  # Replace

    return dp[m][n]


minimum_edit_distace = []
for i in words.words():
    temp_distance = editDistDP(str, i, len(str), len(i))
    minimum_edit_distace.append(temp_distance)

minimum_distance_word = min(minimum_edit_distace)

indices = [i for i in range(len(minimum_edit_distace)) if minimum_edit_distace[i] == minimum_distance_word]

print("the top suggested words along with their minimum edit distances are: ")
for i in indices:
    print(words.words()[i], ": ", minimum_distance_word)
time_end = time.time()

print("the entire time taken is: ", time_end - time_start)
