import random

# two cards drawn. All face cards are of the value 10
# if cards add to over 21, the drawer looses
# the drawer who is as close to 21 wins.
# if both scores are of same value, the dealer wins as the last drawer

suits = ["Clubs","Spades","Diamond","Flower"]

cards_nos = list(range(1,11))

face_cards = ["Q","J","K"]

card_one_suit = cards_nos + face_cards

full_decl = {suit: card_one_suit for suit in suits}

def pick_3_cards():
    return random.choices(card_one_suit,k=3)

def interpret_hand(ls):
    return [element if isinstance(element, int) else 10 for element in ls]

def is_over_21(ls):
    ls = interpret_hand(ls)
    num1, num2 = ls
    return True if num1+num2 > 21 else False


def player_has_won(ls, ls2):
    #interpreting raw results
    ls, ls2 = interpret_hand(ls), interpret_hand(ls2)
    num1, num2 = ls #player 1
    num3, num4 = ls2 #player 2
    return True if num1 + num2 > num3 + num4 else False

play_game = True

while play_game:
    player = pick_3_cards()
    dealer_hand =  pick_3_cards()
    print(f"This is your hand {player}")
    if is_over_21(player):
        print("Sorry, you loose!")
    else:
        print(f"Dealer's first card is {dealer_hand[0]}")
        continue_ = input("Press y to let the dealer get another car: ")
        if continue_ != 'y':
            print("You lost by quitting early!!!")
        else:
            print(f"Your final hand is {player}")
            print(f"Dealer's final hand is {dealer_hand}")
            if is_over_21(dealer_hand):
                print("Congralations! You win as the dealer has exceeded value of 21")
            else:
                if player_has_won(player, dealer_hand):
                    print("Congratulations!!! You won!")
                else:
                    print("Sadly, you loose!")
    continue_ = input("press y to play again : ")
    if continue_ != 'y':
        play_game=False
