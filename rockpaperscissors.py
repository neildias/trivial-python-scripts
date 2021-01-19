import numpy as np

computer_score = []
player_score = []

def first_wins_logic(first, second):
    if first == second:
        return "Draw"
    if first == "r" and second == "s":
        print("Rock breaks Scissors...")
        return True
    if first == "r" and second == "p":
        print("Paper covers rock...")
        return False
    if first == "s" and second == "r":
        print("Rock breaks Scissors...")
        return False
    if first == "s" and second == "p":
        print("Scissors cut papers")
        return True
    if first == "p" and second == "s":
        print("Scissors cut papers")
        return False
    if first == "p" and second == "r":
        print("Paper covers rock...")
        return True

def print_scores():
    if not(player_score) and not (computer_score):
        return
    print("\nFinal scores are:")
    print("================")
    print(f"Player\t\t\t : {sum(player_score)}")
    print(f"Computer\t\t : {sum(computer_score)}")
    if sum(player_score) > sum(computer_score):
        print("You are the overall winner! Well played!")
    elif sum(player_score) < sum(computer_score):
        print("Overall score says I'm the man. Yippee!!!")
    else:
        print("Final result is a draw! I have not been more bored in my life.")

print("Welcome to the game of Rock-Paper-Scissors.""")
rounds = int(input("How many rounds would you like to play? Enter integer.. "))

try:
    for round in range(rounds):
        print("Round {}".format(round+1))
        print("---------")
        temp_choice_holder = ['r', 'p', 's']
        switch=True
        while switch:
            print("Okay! Time to pick Rock-Paper-Scissors. Use just initial alphabets "
                " for choosing anyone of them. Eg. for choosing Rock, type 'r'", end=" ")
            player = input().lower()
            if player in temp_choice_holder:
                switch = False
        computer = np.random.choice( temp_choice_holder, 1 )
        print(f"You chose \t\t\t: {[player]}")
        print(f"Computer chose\t\t: {computer}")
        player_wins = first_wins_logic(player, computer)
        if  player_wins == True:
            print("Good : You win!!!  :-( ")
            player_score.append(1)
        elif player_wins == False:
            print("I WIN. Hurray!!!!")
            computer_score.append(1)
        else:
            print("Its a draw. How boring.")
        print()

except Exception as e:
    print(e)
    print("Invalid input! Please enter only integers.")



print_scores()
