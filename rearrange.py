import random

from sqlalchemy import null


words = input('write words to rearrange:').split()

def rearrange_words():
    random.shuffle(words)
    new_sequence = " ".join(words)
    print(new_sequence)

if __name__ == '__main__':
    quote = rearrange_words()
    print (quote)

