from operator import index
import random
import sys, random
from string import punctuation

from markupsafe import string
from sqlalchemy import null


def histogram(file):
    
    dictionary = {}      #initialize an empty dictionary:  key = word, value = appearance_count

    with open(file, "r") as file:
        for line in file:
            for word in line.split():
                #strip the punctionation from both sides of the word & convert to lowercase
                word = word.lstrip(punctuation).rstrip(punctuation).strip('\n').lower()
                if word not in dictionary:
                    dictionary[word] = 1 
                else:
                    dictionary[word] += 1

    for word in dictionary:
        print(f'{word} = {dictionary[word]}') 

    return dictionary
    

def unique_words(dictionary):

    print(f'\nThere are {len(dictionary)} unique words in this dictionary.\n')
    

def frequency(word, dictionary):

    if word in dictionary:
        print(f'\nThe word {word} appears {dictionary[word]} times in this text.\n')
    else:
        print(f'\nThe word {word} appears 0 times in this text.\n')


def sample(dictionary):

    total_words = sum(dictionary.values())

    #print(f'total words: {total_words}') 

    #generate a random number
    sample_num = random.randrange(0, total_words)
    #print(f'sample_num: {sample_num}')

    #initialize index position and sample word variables
    index_position = 0 
    sample_word = null

    for word in dictionary:
        if index_position <= sample_num:
            index_position += dictionary[word] #add the value for each word to the index position
            sample_word = word #store the most recent word as our sample word
    
    #print(sample_word)
    return sample_word

def test_sample(dictionary, num_tests):
    
    test_num = 0
    file_name = f'histogram - {num_tests} tests.txt'
    f = open(file_name, "a")


    while test_num < num_tests:
        sample_word = sample(dictionary)
        f.write(f'{sample_word}\n')
        test_num += 1

# name is the function being imported // main is the function called on the command line
if __name__ == "__main__":
    dictionary = histogram('fish.txt')
    test_sample(dictionary, 10000)
    histogram('histogram - 10000 tests.txt')
    # unique_words(dictionary)
    # frequency('fish', dictionary)
    # sample(dictionary)