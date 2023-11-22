import random


def hangman():
    word = random.choice(
        ['teacher', 'president', 'engineer', 'nurse', 'friends'])
    valid_letters = 'abcdefghijklmnopqrstuvwxyz'
    print('-'*len(word))
    turns = 10
    guessmade = ''

    while len(word) > 0:
        main = ''
        missed = 0
        for letter in word:
            if letter in guessmade:
                main = main + letter
            else:
                main = main + "_" + " "

        if main == word:
            print(main)
            print("You win")
            break

        print('Guess the word: ', main)
        guess = input()

        if guess in valid_letters:
            guessmade = guessmade + guess
        else:
            print("Enter valid character")
            guess = input()
        if guess not in word:
            turns = turns - 1
            match turns:
                case 9:
                    print("{} turns left".format(turns))
                    break
                case 8:
                    print("{} turns left".format(turns))
                    break
                case 7:
                    print("{} turns left".format(turns))
                    break
                case 6:
                    print("{} turns left".format(turns))
                    break
                case 5:
                    print("{} turns left".format(turns))
                    break
                case 4:
                    print("{} turns left".format(turns))
                    break
                case 3:
                    print("{} turns left".format(turns))
                    break
                case 2:
                    print("{} turns left".format(turns))
                    break
                case 1:
                    print("{} turns left".format(turns))
                    break
                case 0:
                    print("{} turns left".format(turns))
                    print("you killed a kind man")
                    break
                case _:
                    print("hmm not found")
        break


name = input('Enter your name: ')
print("Welcome {}".format(name))
print("-"*50)
print("Trying guessing the word in 10 tries")

hangman()
