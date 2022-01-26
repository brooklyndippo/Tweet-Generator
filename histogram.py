import random
import sys, random
from string import punctuation

class histo_word:
    def __init__ (self, word, count):
        self.word = word
        self.count = count


def histogram(file):

    #take in a text file as an argument
    #file = sys.argv[1]
    
    #open the file and read it 
    file = open(file, "r")

    #separate into words at each space
    words = file.read().split(" ")
    

    #initialize an empty dictionary
    #key = word, value = appearance count
    dictionary = {}

    #remove any punctuation from beginning/end of words 
    for word in words:
        #strip the punctionation from both sides of the word & convert to lowercase
        word = word.lstrip(punctuation).rstrip(punctuation).lower()
        if word not in dictionary:
            dictionary[word]=1 
        else:
            dictionary[word] += 1


    for word in dictionary:
        print(f'{word} = {dictionary[word]}') 

    unique_words(dictionary)

    frequency('bad', dictionary)
    

def unique_words(dictionary):

    #unique words = length of the dictionary
    print(f'\nThere are {len(dictionary)} unique words in this dictionary.\n')
    

def frequency(word, dictionary):
    
    #find the key value pair in the dictionary
    print(f'\nThe word {word} appears {dictionary[word]} times in this text.\n')



# name is the function being imported // main is the function called on the command line
if __name__ == "__main__":
    histogram('lorax.txt')
