import random
import sys, random

def random_dict_words():

    #default file is the dictionary if not declared 
    file = "/usr/share/dict/words"

    #take in the argument for number of words to pull from the dictionary
    num_words = int(sys.argv[1])
    
    #open the dictionary file and separate into a list at each line break
    dict = open(file, "r")
    lines = dict.read().splitlines()

    #initialize an empty array for our random words
    random_words = []

    #add n random words into our array
    num = 0
    while num < num_words:
        line = lines[random.randint(0, 235886)]
        random_words.append(line)
        num += 1

    #print the words in a "sentence"
    random_sentence = " ".join(random_words)
    print(random_sentence)

    dict.close()

# name is the function being imported // main is the function called on the command line
if __name__ == "__main__":
    random_dict_words()

