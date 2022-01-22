import random

#from sqlalchemy import null

def rearrange_words():
    words = input('write words to rearrange:').split()
    random.shuffle(words)
    new_sequence = " ".join(words)
    print(new_sequence)

if __name__ == '__main__':
    rearrange_words()

