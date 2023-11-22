import random
#choosig a random item in the list
rand = random.choice(['apple', 'banana', 'kiwi'])
print(rand)

#return a random list of elements
sample = random.sample(range(100), 10) 
print(sample)

#choose a random  floating number between 0 and 1
print(random.random())

#choosing number from a range 
#the randrange() accepts arguments just like the range()
random.randrange(8)

