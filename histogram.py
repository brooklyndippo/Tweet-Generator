import random
import sys, random
from string import punctuation

from markupsafe import string


def histogram(file):
    
    #initialize an empty dictionary:  key = word, value = appearance_count
    dictionary = {}

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
    
    unique_words(dictionary)

    frequency('fish', dictionary)

    sample(dictionary)
    

def unique_words(dictionary):

    #unique words = length of the dictionary
    print(f'\nThere are {len(dictionary)} unique words in this dictionary.\n')
    

def frequency(word, dictionary):
    if word in dictionary:
        print(f'\nThe word {word} appears {dictionary[word]} times in this text.\n')
    else:
        print(f'\nThe word {word} appears 0 times in this text.\n')


def sample(dictionary):

    total_words = sum(dictionary.values())

    print(f'total words: {total_words}') 

    sample_num = random.randint(0, total_words)




# name is the function being imported // main is the function called on the command line
if __name__ == "__main__":
    histogram('fish.txt')
