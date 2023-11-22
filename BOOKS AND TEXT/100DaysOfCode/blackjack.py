import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
player_cards = []
dealer_cards = []
sum_of_player_cards: int = 0
sum_of_dealer_cards: int = 0


def random_number(arr: list):
    return random.randint(0, len(arr)-1)


def select_initial_cards(cards: list):
    player_cards = []
    for _ in range(1, 3):
        card = cards[random_number(cards)]
        player_cards.append(card)
    return player_cards


def add_cards(cards: list) -> int:
    total: int = 0
    for i in range(0, len(cards)):
        total += cards[i]
    return total


player_cards = select_initial_cards(cards)
dealer_cards = select_initial_cards(cards)
sum_of_dealer_cards = add_cards(dealer_cards)
sum_of_player_cards = add_cards(player_cards)

def findItem(arr: list,num: int)->int:
    return arr.index(num,0,len(arr))

def blackjack_winner(dealer: int, player: int,player_cards: list):
    ace =11
    if dealer == 21 or player ==21:
        if player == 21:
            print("Player wins")
        elif dealer ==21:
            print("Player lose")
        else:
            # Do nothing here
            pass
    elif player > 21:
        if ace not in player_cards:
            print("Player lose")
        else:
            pass








