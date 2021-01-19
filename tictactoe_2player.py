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


def show_grid_no():
    grid_map = {1: '1', 2: '2', 3: '3',
                4: '4', 5: '5', 6: '6',
                7: '7', 8: '8', 9: '9'}

    print(f'''

                            |     |
                         1  |  2  |  3
                       _____|_____|_____
                            |     |
                         4  |  5  |  6
                       _____|_____|_____
                            |     |
                         7  |  8  |  9
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


def game_over_display(a, b, c, whichplayer, choice):
    display(reset=True, winners_mark=choice, winning_grids=(a, b, c))
    print(f"{whichplayer} Wins!!! See winning grids above.")
# ----------------begin program-------------------

# inputs
draw = True
print("Do you choose to play Xs or 0s? :")
while True:
    player_choice = input().lower()
    if player_choice in ['x', 'o']:
        break
    print("Wrong input. Type either x or o. Lets try again... Type here: ")

#welcome prints
print(f"player 1 choice is {player_choice}")
player2_choice = 'x' if player_choice == 'o' else 'o'
print(f"player 2 choice is {player2_choice}")
player_selection = ['o'] * 5 if player_choice == 'o' else ['x'] * 5
player2_selection = ['x'] * 5 if player_choice == 'o' else ['o'] * 5

print("\nThe game will be played on the following board.")
print("Please make a special note of the squares and their corresponding "
      " number on the board.")

show_grid_no()

# game
for i in range(9):
    #inputs
    player = "Player1" if i%2==0 else "Player2"
    while True:
        print(f"\n{player}: ")
        grid_chosen = input(f"Which box do you want to mark {grid} - dont repeat choice :: ")
        if grid_chosen in grid: break
        print(f"Wrong input: please choose from : {grid}")

    if player == 'Player1':
        cross_and_zero(grid_chosen, player_choice)
        if gameOver(player_choice):
            a, b, c = gameOver(player_choice)
            game_over_display(a,b,c,player,choice=player_choice)
            draw = False
            break
    else:
        cross_and_zero(grid_chosen, player2_choice)
        if gameOver(player2_choice):
            a, b, c = gameOver(player2_choice)
            game_over_display(a, b, c, player,choice=player2_choice)
            draw = False
            break

if draw:
    print("\nAh! this is a draw. How boring!!!. :(")
print("\nThanks for playin'! Bye!!!")
