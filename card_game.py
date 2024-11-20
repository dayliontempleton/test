import os
import random
from colorama import Fore, Back, Style

os.system("clear")

#setup the game
suits = ("Hearts",  "Clubs", "Diamonds", "Spades")
numbers = (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)

# define player hands
player1_card = []
player2_card = []

#define player packs
player1_pack = []
player2_pack = []

#create deck of cards
def create_deck():
    deck = []

    for suit in suits:
        for number in numbers:
            card = (number, suit)
            deck.append(card)
    random.shuffle(deck)
    return deck

#process cards
def process_card(card_number):
    if card_number == 11:
        return "Jack"
    elif card_number == 12:
        return "Queen"
    elif card_number == 13:
        return "King"
    elif card_number == 14:
        return "Ace"
    else:
        return card_number

#create deck
deck_of_cards = create_deck()

#main game looop
while len(deck_of_cards) > 1:
    # prompt
    input("press enter to deal cards")

    #deal cards and remove them from pack
    player1_card = random.choice(deck_of_cards)
    deck_of_cards.remove(player1_card)
    player2_card = random.choice(deck_of_cards)
    deck_of_cards.remove(player2_card)

    os.system("clear")

    #display cards
    if player1_card[0] > player2_card[0]:
        print(f"{Fore.GREEN}Player 1 card: { process_card(player1_card[0])} of {player1_card[1]}")
        print(f"{Fore.RED}Player 2 card: { process_card(player2_card[0])} of {player2_card[1]}")
        print(Style.RESET_ALL)
    elif player1_card[0] < player2_card[0]:
        print(f"{Fore.RED}Player 1 card: { process_card(player1_card[0])} of {player1_card[1]}")
        print(f"{Fore.GREEN}Player 2 card: { process_card(player2_card[0])} of {player2_card[1]}")
        print(Style.RESET_ALL)
    else:
        print(f"{Fore.GREEN}Player 1 card: { process_card(player1_card[0])} of {player1_card[1]}")
        print(f"{Fore.GREEN}Player 2 card: { process_card(player2_card[0])} of {player2_card[1]}")
        print(Style.RESET_ALL)

    #compare
    if player1_card[0] > player2_card[0]:
        print(f"{Fore.YELLOW}Player 1 wins this hand!{Style.RESET_ALL}")
        player1_pack.append(player1_card)
        player1_pack.append(player2_card)
    elif player1_card[0] < player2_card[0]:
        print(f"{Fore.YELLOW}Player 2 wins this hand!{Style.RESET_ALL}")
        player2_pack.append(player1_card)
        player2_pack.append(player2_card)
    else:
        print(f"{Fore.YELLOW}It's a draw!{Style.RESET_ALL}")
        player1_pack.append(player1_card)
        player2_pack.append(player2_card)
    
    #display number of cards
    print(f"\n{Fore.BLUE}Number of cards left: {len(deck_of_cards)}{Style.RESET_ALL}")
    print(f"Player 1 Pack: {len(player1_pack)} cards.")
    print(f"Player 2 Pack: {len(player2_pack)} cards.")
    print("")
print(f"{Style.RESET_ALL}")

#check winner
if len(player1_pack) > len(player2_pack):
    print(f"{Fore.YELLOW}Player 1 wins the game with {len(player1_pack)} cards over {len(player2_pack)} cards!")
elif len(player1_pack) < len(player2_pack):
    print(f"{Fore.YELLOW}Player 2 wins the game with {len(player2_pack)} cards over {len(player1_pack)} cards!")
else:
    print(f"{Fore.YELLOW}It's a Draw!")

print(f"{Style.RESET_ALL}")

