from BlackjackArt import logo
import random

print(logo)
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
game_on = True
def deal():
    """deals for both computer and player"""
    my_cards = []
    comp_cards = []
    all_cards = [my_cards, comp_cards]
    for card in range(2):
        my_cards.append(random.choice(cards))
        comp_cards.append(random.choice(cards))
    print(f"Your cards: {my_cards}, current score: {sum(my_cards)}")
    print(f"Computer's first card: {comp_cards[0]},")
    return all_cards

allcards = deal()
def 
    
while game_on == True:
    do_yu = input("Do you want to play a game of Blackjack? Type 'y' or 'n'")
    if do_yu == "n" :
        game_on = False  
        break
    deal()
    
         
    
    












