import json
from difflib import get_close_matches
data = json.load(open('./dict.json', 'r'))


def translate(word, data):
    word = word.lower()
    # print(word)
    words = []
    # print(text)
    if word in data:
        print(data[word])
    elif len(get_close_matches(word, data.keys())) > 1:
        print(data.keys(word))
        # words.append(data[word])
        # for x in words:
        #     print(x)
    else:
        print('Word not found!')
    return None


word = input("Enter word to search: ")
output = translate(word, data)
print(output)

# NOTE: returning the first two elements of the dictionary
# convert the dictionary key-value pair using the dict.items() method.
# convert to list using the list built-in function and access the list using square brackets
# convert the list to dictionary using the dict built-in function


# first_two = dict(list(data.items())[:2])
# print(first_two)
