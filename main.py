import random

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_scores(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if sum(cards) > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(u_score, c_score):
    if u_score == c_score:
        return "Draw"
    elif c_score == 0:
        return "Lose, opponent has Blackjack"
    elif u_score == 0:
        return "Win, you have Blackjack"
    elif u_score > 21:
        return "You went over, you lose."
    elif c_score > 21:
        return "Opponent went over, you win."
    elif u_score > c_score:
        return "You win"
    else:
        return "You lose"



def play_game():
    user_cards = []
    computer_cards = []

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())


    game_is_over = False
    while not game_is_over:
        user_score = calculate_scores(user_cards)
        computer_score = calculate_scores(computer_cards)
        print(f"{user_cards} = {user_score}")
        print(f"first card: {computer_cards[0]}")



        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_is_over = True
        else:
            user_deal = input("Do you want another card? y or n: ")
            if user_deal == "y":
                user_cards.append(deal_card())
            else:
                game_is_over = True


    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_scores(computer_cards)
        print(f"{computer_cards} = {computer_score}")

    print(compare(user_score,computer_score))

while input("Do you wanna play? y or n: ") == "y":
    print("\n" * 2)
    play_game()

