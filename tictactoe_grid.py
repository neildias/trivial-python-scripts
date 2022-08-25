def generate_grid():
    verticle_pattern_rows = lambda:[" ", " ", " ", "|", " ", " ", " ", "|", " ", " ", " "] 
    horizontal_pattern_rows = lambda:["-" for i in range (11)]
    return [verticle_pattern_rows() if not i in [3,7] else horizontal_pattern_rows() for i in range(11)]

# create another function that updates and formats the list

def update_and_display(choice: int, arr: "listlike", X_0: str):
    if choice == 1:
        arr[1][1] =  X_0
    elif choice == 2:
        arr[1][5] =  X_0
    elif choice == 3:
        arr[1][9] =  X_0
    elif choice == 4:
        arr[5][1] =  X_0
    elif choice == 5:
        arr[5][5] =  X_0
    elif choice == 6:
        arr[5][9] =  X_0
    elif choice == 7:
        arr[9][1] =  X_0
    elif choice == 8:
        arr[9][5] =  X_0
    elif choice == 9:
        arr[9][9] =  X_0
        
    # display      
    print_result(arr)

# create basic display function that prints the above list in a way that resembles a tictactoe board

def print_result(array):
    for arr in array:
        for element in arr:
            # the following line is not needed for this function, but it will 
            # become useful later when we use numpy
            element = element if not element == "0" else " "
            print(element, end="  ")
        print()

grid = generate_grid()

print_result(grid)
