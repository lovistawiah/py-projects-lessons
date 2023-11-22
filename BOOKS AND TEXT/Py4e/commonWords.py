# opens a file
fhand = open("intro.txt")
di = dict()
lst = list()
# read every line in the file
for line in fhand:
    # removes whitespace off the right side of the end of the line
    line.rstrip()
    # split and place every word on every line as an element of a list
    words = line.split()
    for word in words:
        # loop through every word and update the counting of the word default is 0
        di[word] = di.get(word, 0) + 1

for k, v in di.items():
    # add tuples to end of the array
    lst.append((v, k))
# sort the list of items placing the highest value or number at index 0
lst = sorted(lst, reverse=True)

# shorter of appending and sorting the key value-pair in the dictionary

# FIXME: Cannot print out the most frequent word and highest number
# lst = sorted([(k, v) for k, v in di.items()], reverse=True)

for v, k in lst[:10]:
    print(k, v)
