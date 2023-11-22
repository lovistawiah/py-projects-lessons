counts = dict()
bigWord = ""
bigCount = -1
fname = input('Enter file name: ')
if len(fname) < 1:
    handle = open('clown.txt')
else:
    handle = open(fname)

for line in handle:
    # print(line)
    line.rstrip()
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1


for k, v in counts.items():
    # print(k, v)
    if v > bigCount:
        bigCount = v
        bigWord = k


print(f'Frequent word:{bigWord} and highest number:{bigCount}')
