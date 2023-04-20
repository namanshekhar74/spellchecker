from nltk.corpus import words
import numpy as np
import time

# f = open("corpus.txt", "r")
# r = f.readlines()
# 
# dictionary_words = []
# 
# for i in r:
#     dictionary_words.append(i)


str = input("please enter the word: ")

str = str.replace(" ", "")

time_start = time.time()


def n_gram(word, n):
    n_gram = []
    for i in range(0, len(word) - n + 1):
        temp = word[i:i + n]
        n_gram.append(temp)
    return n_gram


gram = int(input("please enter n for n_gram checking: "))

word_check_ngram = n_gram(str, gram)

print("the n-gram of the input word is: ", word_check_ngram)

similarity = []


for i in words.words():
    intersection = 0
    for j in word_check_ngram:
        if j in i:
            intersection += 1
    if(len(i) - gram + 1 >= 0) :
        union = len(word_check_ngram) + len(i) - gram + 1 - intersection  # here is the change needed to be made for n-gram
        sim = intersection / union
        similarity.append(sim)

top_20_idx = np.argsort(similarity)[-20:]
top_words = []
for i in top_20_idx:
    top_words.append(words.words()[i])
top_words = top_words[::-1]
print("the top 20 words are: ", top_words)


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
for i in top_words:
    temp_distance = editDistDP(str, i, len(str), len(i))
    minimum_edit_distace.append(temp_distance)
print("the minimum edit distances of the words with ", str, " are: ", minimum_edit_distace)
time_end = time.time()
minimum_distance_word = min(minimum_edit_distace)

indices = [i for i in range(len(minimum_edit_distace)) if minimum_edit_distace[i] == minimum_distance_word]

print("the top suggested words along with their minimum edit distances are: ")
for i in indices:
    print(top_words[i], ": ", minimum_distance_word)

print("the entire time taken is: ", time_end - time_start)

