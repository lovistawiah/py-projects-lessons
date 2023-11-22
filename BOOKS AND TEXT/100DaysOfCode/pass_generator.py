# Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")

try:
    nr_letters = int(
        input("How many letters would you like in your password?\n"))
    nr_symbols = int(input(f"How many symbols would you like?\n"))
    nr_numbers = int(input(f"How many numbers would you like?\n"))

# Eazy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91
    if nr_letters > len(letters):
        print("input cannot exceed number of alphabets")
    elif nr_symbols > len(symbols):
        print("input cannot exceed number of symbols")
    elif nr_numbers > len(numbers):
        print("input cannot exceed numbers")
    else:
        password = ''
        for i in range(0, nr_letters):
            selected_letters = random.randint(0, len(letters)-1)
            password += letters[selected_letters]

        for i in range(0, nr_symbols):
            nr_symbols = random.randint(0, len(symbols)-1)
            password += symbols[nr_symbols]

        for i in range(0, nr_numbers):
            nr_numbers = random.randint(0, len(numbers)-1)
            password += numbers[nr_numbers]

        # Hard Level - Order of characters randomised:
        # e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
        pass_arr = []
        randomised_pass = ''
        for char in password:
            pass_arr.append(char)

        randomised_pass = random.sample(pass_arr, len(pass_arr))
        randomised_pass = ''.join(randomised_pass)
        print(password)
        print(randomised_pass)
except ValueError:
    print("Inputted value is not an integer")
