# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}


import re

def read_file_content(filename):
    # [assignment] Add your code here 

    try:
        file = open(filename, 'rt')
        text = file.read()
        file.close()
    except Exception:
        return Exception
    
    return text


def count_words():
    text = read_file_content("./story.txt")
    # [assignment] Add your code here
    
    for character in text:
        if not(character.isalpha() or character.isnumeric() or character.isspace()):
            text = text.replace(character, "")


    text = text.split()

    word_count = []

    for word in text:
        word_count.append(len(word))

    text_dictionary = dict(zip(text, word_count))

    return text_dictionary

print(count_words())