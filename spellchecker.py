from nltk.corpus import words
import time

str = input("please enter the word: ")

str = str.replace(" ", "")

time_start = time.time()

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

n_gram_dict = {new_list: [] for new_list in word_check_ngram}
# n_gram_dict["qw"].append("sada")
# print(n_gram_dict)

qualified_words = []
qualified_words_dict = {}
for i in words.words():
    for j in word_check_ngram:
        if set(word_check_ngram).intersection(n_gram(i, gram)):
            if j in i:
                n_gram_dict[j].append(i)
                if i in qualified_words_dict:
                    qualified_words_dict[i] += 1
                else:
                    qualified_words_dict[i] = 1

print()


sorted_dict = sorted(qualified_words_dict.items(), key=lambda x: x[1], reverse=True)
sorted_dict = dict(sorted_dict)

temp = list(sorted_dict)
top_20_words = []
for i in range(20):
    top_20_words.append(temp[i])
print(top_20_words)


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
for i in top_20_words:
    temp_distance = editDistDP(str, i, len(str), len(i))
    minimum_edit_distace.append(temp_distance)
print("the minimum edit distances of the words with ", str," are: ", minimum_edit_distace)
time_end = time.time()

minimum_distance_word = min(minimum_edit_distace)

indices = [i for i in range(len(minimum_edit_distace)) if minimum_edit_distace[i] == minimum_distance_word]

print("the top suggested words along with their minimum edit distances are: ")
for i in indices:
    print(top_20_words[i], ": ", minimum_distance_word)

print("the entire time taken is: ", time_end - time_start)
