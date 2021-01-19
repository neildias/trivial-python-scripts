grid = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
# make a dictionary
grid_map = {1: ' ', 2: ' ', 3: ' ',
            4: ' ', 5: ' ', 6: ' ',
            7: ' ', 8: ' ', 9: ' '}

def gameOver(player1sMark):  # x  or 0
    winner = 0
    winning_grid_identifier = 0
    if (grid_map[1] == grid_map[2] == grid_map[3]):
        winner = grid_map[1]
        winning_grid_identifier = 1
        winning_grid = 1, 2, 3

    elif (grid_map[4] == grid_map[5] == grid_map[6]):
        winner = grid_map[4]
        winning_grid_identifier = 2
        winning_grid = 4, 5, 6

    elif (grid_map[7] == grid_map[8] == grid_map[9]):
        winner = grid_map[7]
        winning_grid_identifier = 3
        winning_grid = 7, 8, 9

    elif (grid_map[1] == grid_map[4] == grid_map[7]):
        winner = grid_map[1]
        winning_grid_identifier = 4
        winning_grid = 1, 4, 7

    elif (grid_map[2] == grid_map[5] == grid_map[8]):
        winner = grid_map[2]
        winning_grid_identifier = 5
        winning_grid = 2, 5, 8

    elif (grid_map[3] == grid_map[6] == grid_map[9]):
        winner = grid_map[3]
        winning_grid_identifier = 6
        winning_grid = 3, 6, 9

    elif (grid_map[3] == grid_map[5] == grid_map[7]):
        winner = grid_map[3]
        winning_grid_identifier = 7
        winning_grid = 3, 5, 7

    elif (grid_map[1] == grid_map[5] == grid_map[9]):
        winner = grid_map[1]
        winning_grid = 1, 5, 9

    # to skip default " "
    if winner == " ":
        return False
    if winner == player_choice:
        return winning_grid
    elif winner == player2_choice:
        return winning_grid
    return False


def display(reset=False, winners_mark=None, winning_grids=None):
    global grid_map

    if reset:
        # make a dictionary
        grid_map = {1: ' ', 2: ' ', 3: ' ',
                    4: ' ', 5: ' ', 6: ' ',
                    7: ' ', 8: ' ', 9: ' '}
        if winners_mark:
            for grd in winning_grids:
                grid_map[grd] = winners_mark


    print(f'''

                            |     |
                         {grid_map[1]}  |  {grid_map[2]}  |  {grid_map[3]}
                       _____|_____|_____
                            |     |
                         {grid_map[4]}  |  {grid_map[5]}  |  {grid_map[6]}
                       _____|_____|_____
                            |     |
                         {grid_map[7]}  |  {grid_map[8]}  |  {grid_map[9]}
                            |     |''')


def cross_and_zero(grid_no, x_or_0):
    global grid_map, grid
    if grid_no == '1':
        grid_map[1] = x_or_0
        grid.remove('1')

    elif grid_no == '2':
        grid_map[2] = x_or_0
        grid.remove("2")

    elif grid_no == '3':
        grid_map[3] = x_or_0
        grid.remove("3")

    elif grid_no == '4':
        grid_map[4] = x_or_0
        grid.remove("4")

    elif grid_no == '5':
        grid_map[5] = x_or_0
        grid.remove("5")

    elif grid_no == '6':
        grid_map[6] = x_or_0
        grid.remove("6")

    elif grid_no == '7':
        grid_map[7] = x_or_0
        grid.remove("7")

    elif grid_no == '8':
        grid_map[8] = x_or_0
        grid.remove("8")

    elif grid_no == '9':
        grid_map[9] = x_or_0
        grid.remove("9")

    display()


# ----------------begin program-------------------

# inputs
print("Do you choose to play Xs or 0s? :")
while True:
    player_choice = input().lower()
    if player_choice in ['x', 'o']:
        break
    print("Wrong input. Type either x or o. Lets try again... Type here: ")
print(f"player 1 choice is {player_choice}")
player2_choice = 'x' if player_choice == 'o' else 'o'
print(f"player 2 choice is {player2_choice}")
player_selection = ['o'] * 5 if player_choice == 'o' else ['x'] * 5
#print(f"player 2 selection is {player_selection}")
player2_selection = ['x'] * 5 if player_choice == 'o' else ['o'] * 5
#print(f"player 2 selection is {player2_selection}")

# game
for i in range(5):
    # player 1
    # input sanity
    while True:
        print("Player 1: ")
        grid_chosen = input("Which row do you want to mark [1-9] -dont repeat choice :")
        if grid_chosen in grid:
            break
        print(f"Wrong input: please choose from : {grid}")

    cross_and_zero(grid_chosen, player_choice)

    # win check

    if gameOver(player_choice):
        a, b, c = gameOver(player_choice)
        display(reset=True, winners_mark=player_choice, winning_grids=(a, b, c))
        print("Player 1 Wins!!! See winning grids above.")
        break

    if i == 5: break  # since 2 inputs per loop so 4.5 loops needed
    # player2
    # input sanity
    while True:
        print("Player 2: ")
        grid_chosen2 = input("Which row do you want to mark [1 -9]")
        if grid_chosen2 in grid:
            break
        print(f"Wrong input: please choose from : {grid}")

    cross_and_zero(grid_chosen2, player2_choice)
    # win check

    if gameOver(player_choice):
        a, b, c = gameOver(player_choice)
        display(reset=True, winners_mark=player2_choice, winning_grids=(a, b, c))
        print("Player 2 Wins!!! See winning grids above.")
        break

print("Thanks for playin'! Bye!!!")