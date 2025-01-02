# 100 Days of code
# Day 11 Project: Blackjack
# 1/1/2025

import random


def deal_card():
    """Returns a random cards from the list of cards."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(player_cards):
    """Takes each player cards to calculate thier scores."""
    if sum(player_cards) == 21 and len(player_cards) == 2:
        return 0
    
    if 11 in player_cards and sum(player_cards) > 21:
        player_cards.remove(11)
        player_cards.append(1)
        
    return sum(player_cards)

def compare(u_score, c_score):
    """Takes user and computer scores to pick the winner."""
    if u_score == c_score:
        return "Draw 🙃"
    elif c_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif u_score == 0:
        return "Win with a Blackjack 😎"
    elif u_score > 21:
        return "You went over. You lose 😭"
    elif c_score > 21:
        return "Opponent went over. You win 😁"
    elif u_score > c_score:
        return "You win 😃"
    else:
        return "You lose 😤"
    

def play_game():
    """Starts play the game of Blackjack."""
    user_cards = []
    computer_cards = []
    user_score = -1
    computer_score = -1
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())


    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"Your cards: {user_cards}, Your score: {user_score}.")
        print(f"Computer's first hand: {computer_cards[0]}, Computer's score: {computer_score}.")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card. Type 'n' to pass: ")
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score > 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"YOUR FINAL HAND: {user_cards}, YOUR FINAL SCORE: {user_score}.")
    print(f"COMPUTER'S FINAL HAND: {computer_cards}, COMPUTER'S FINAL SCORE: {computer_score}.")
    print(compare(user_score, computer_score))

while input("Do you want to play a Blackjack game? Type 'y' or 'n': ") == "y":
    play_game()

