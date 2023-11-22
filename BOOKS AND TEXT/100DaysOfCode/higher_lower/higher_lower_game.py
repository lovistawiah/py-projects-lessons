from random import choice
from game_data import data
from art import logo, vs
ask = True
score = 0
continue_game = True


def format_account(account: list, letter: str) -> str:
    string = ""
    acc_name = account['name']
    acc_desc = account['description']
    acc_co = account['country']
    if acc_desc.strip().startswith('A'):
        string = f"Compare {letter}: {acc_name}, an {acc_desc} from {acc_co}"
    else:
        string = f"Compare {letter}: {acc_name}, a {acc_desc} from {acc_co}"
    return string


def check_followers(account_a: dict, account_b: dict) -> dict:
    have_more_followers = input("Type 'a' or 'b': ")
    options = {}
    if have_more_followers == 'a':
        options['boolean'] = account_a['follower_count'] > account_b['follower_count']
        options['acc'] = account_a
    elif have_more_followers == 'b':
        options['boolean'] = account_a['follower_count'] < account_b['follower_count']
        options['acc'] = account_b
    else:
        print("Choose wrong letter")
    return options


while continue_game:
    print(logo)
    score = 0
    while ask:
        if score > 0:
            acc_a = answer['acc']
        else:
            acc_a = choice(data)

        acc_b = choice(data)
        if acc_b == acc_a:
            acc_b = choice(data)

        account_a = format_account(acc_a, 'A')
        account_b = format_account(acc_b, 'B')
        print(account_a)
        print(vs)
        print(account_b)
        answer = check_followers(acc_a, acc_b)
        if answer['boolean'] == True:
            score += 1
            print(score)
        else:
            print(f" Your scored: {score}")
            ask = False

    play_again = input("Do you want to play again 'y' or 'n': ")
    if play_again == 'y':
        continue_game = True
        ask = True
    elif play_again == 'n':
        print("Thanks for playing")
        continue_game = False
    else:
        print("Game Over, you chose wrong option")
        continue_game = False
