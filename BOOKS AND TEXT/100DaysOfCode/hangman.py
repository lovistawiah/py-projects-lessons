# Step 1
import random
word_list = ["ardvark", "baboon", "camel"]

# TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
random_int = random.randint(0, len(word_list)-1)
print(random_int)
random_word = word_list[random_int]


# TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
print(f"Pssst, the solution is {random_word}")
letter = input("Guess a letter: ").lower()

display = list()
rand_word_list = list()
# 01234
# apple
for num in range(0, len(random_word)):
    display.append("_")

for char in random_word:
    rand_word_list.append(char)


        # TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
for rand_letter in random_word:
    if letter == rand_letter:
        print(True)
    else:
        print(False)
