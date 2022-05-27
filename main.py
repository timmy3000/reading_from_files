# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}


def read_file_content(filename):
    # [assignment] Add your code here 

    text = ""
    
    with open(filename, 'rt') as file:
        text = file.read()
    
    return text


def indexOf(arr, delimiter):

    for i in range(len(arr)):
        if arr[i] == delimiter:
            return i

    return -1


def count_words():
    text = read_file_content("./story.txt")
    # [assignment] Add your code here
    
    for character in text:
        if not(character.isalpha() or character.isnumeric() or character.isspace()):
            text = text.replace(character, "").lower()


    text = text.split()

    text_dictionary = {}
    count = 0

    find = ""

    while len(text) > 0:
        find = text[0]

        while indexOf(text, find) != -1:
            count += 1
            del text[indexOf(text, find)]


        text_dictionary[find] = count
        count = 0


    return text_dictionary

print(count_words())
