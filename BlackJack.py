import random
from replit import clear

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate_score(l):
    if sum(l) == 21 and len(l) == 2:
        return 0
    if sum(l) > 21 and 11 in l:
        l.remove(11)
        l.append(1)
    return sum(l)

def compare(user_score, comp_score):
    if comp_score == 0:
        return 'Lose, Computer has a blackjack😒'
    elif user_score == 0:
        return 'Win, You have a blackjack😁'
    elif user_score > 21:
        return "Lose, You went over 21😢"
    elif comp_score > 21:
        return "Win, Computer went over 21😉"
    elif user_score == comp_score:
        return "Draw😑"
    elif user_score > comp_score:
        return "Win😎"
    else:
        return "Lose😭"

def blackjack():
    print(logo)
    user = []
    comp = []
    
    # initial assignment of 2 cards each to user & comp
    for _ in range(2):
        user.append(deal_card())
        comp.append(deal_card())
    
    # user plays
    game_over = False
    while not game_over:
        # score calculation
        user_score = calculate_score(user)
        comp_score = calculate_score(comp)
    
        print(f"    Your cards: {user}, current score: {user_score}")
        print("    Computer's first card:", comp[0])
    
        # blackjack
        if user_score == 0 or comp_score == 0 or user_score > 21:
            game_over = True

        # user continues 
        else:
            another = input("Type 'y' to get another card, type 'n' to pass: ")
            if another == 'y':
                user.append(deal_card())
            else:
                game_over = True
    
    # comp plays
    while comp_score != 0 and comp_score < 17:
        comp.append(deal_card())
        comp_score = calculate_score(comp)
    
    # final scores and comparison
    print(f"    Your final hand: {user}, final score: {user_score}")
    print(f"    Computer's final hand: {comp}, final score: {comp_score}")
    print('\n' + compare(user_score, comp_score))

while input("Do you want to play a game of blackjack? Type 'y' or 'n': ") == 'y':
    clear()
    blackjack()