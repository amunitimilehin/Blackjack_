from BlackjackArt import logo
import random


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
def deal():
    """deals for both computer and player"""
    my_cards = []
    comp_cards = []
    for card in range(2):
        my_cards.append(random.choice(cards))
        comp_cards.append(random.choice(cards))
    # print(f"Your cards: {my_cards}, current score: {sum(my_cards)}")
    # print(f"Computer's first card: {comp_cards[0]},")
    all_cards = [my_cards, comp_cards]
    return all_cards


allcards = deal()



def update_cards():
    """adds new cards to each player"""
    allcards[0].append(random.choice(cards))
    allcards[1].append(random.choice(cards))
    print(f"Your cards: {allcards[0]}, current score: {sum(allcards[0])}")
    print(f"Computer's first card: {allcards[1][0]},")
    
    
    
while input("Do you want to play a game of Blackjack? Type 'y' or 'n'") == "y":
    print(logo)
    deal()
    print(f"Your cards: {allcards[0]}, current score: {sum(allcards[0])}")
    print(f"Computer's first card: {allcards[1][0]},")
    while input("Type 'y' to get another card, type 'n to pass'") == "y":
        update_cards()
    
         
    
    












