import random
import sys, random

#take in the argument for number of words to pull from the dictionary
num_words = int(sys.argv[1])

#open the dictionary file and separate into a list at each line break
dict = open("./basic_dict.txt", "r")
lines = dict.read().splitlines()

#initialize an empty array for our random words
random_words = []

#add n random words into our array
num = 0
while num < num_words:
    line = lines[random.randint(0,23)]
    random_words.append(line)
    num += 1

#print the words in a "sentence"
random_sentence = " ".join(random_words)
print(random_sentence)

# print the random words as a list
# for word in random_words:
#     print(word)