#for fibonacci function
#since pythons LEGB seems to scope based on where the function is created, not where it is called
a, b = 0, 1

def fibonacci_error(x):
    try:
        if x < 0 : return True
    except: return True

def erase_stored_values():
    global a, b
    a, b = 0, 1

def fibonacci_generator():
    global a, b
    a, b = b, a + b
    while True:
        yield b

def get_reusable_fibonacci(endNum):
    '''Returns index and the corresponding fibonacci number as a dictionary'''
    if fibonacci_error(endNum): return "Invalid input! Input must be positive integers."
    fibonacci_db = {1:0,2:1}
    for fibonacci_index in range(3, endNum+1):
        fibonacci_db[fibonacci_index] = next(fibonacci_generator())
    erase_stored_values()
    return fibonacci_db

def fibonacci_recurcive(n=10, first_pass=True, fibonacci_db=None, prints=True):
    '''This does not store values hence memory used is neglibible'''
    if fibonacci_error(n): return "Invalid input! Input must be positive integers."
    global a, b

    #first pass logic
    if first_pass and n==2: return [0, 1]
    if first_pass and n==1: return [0]
    if not fibonacci_db: fibonacci_db = [0, 1]
    else: fibonacci_db = fibonacci_db

    #recursion terminator clause
    if n == 0:
        erase_stored_values()
        return fibonacci_db
    if first_pass:
        if prints: print("{} {}".format(a,b), end=" ")
        n -= 2
    a, b = b, a+b
    if prints: print(b, end=" ")
    fibonacci_db.append(b)
    return fibonacci_recurcive(n-1, first_pass=False, fibonacci_db=fibonacci_db, prints=prints)

def get_ith_fibonacci(n):
    #use get_reusable_fibonacci
    if fibonacci_error(n): return "Invalid input! Input must be positive integers."
    for index in range(3,n+1):
        number = next(fibonacci_generator())
        #n-1 as python indexing starts from zero
        if index == n:
            erase_stored_values()
            return number

def get_upto_ith_fibonacci(x):
    if fibonacci_error(x): return "Invalid input! Input must be positive integers."
    return get_reusable_fibonacci(x)

def fibonacci_checker(x):
    if fibonacci_error(x): return "Invalid input! Input must be positive integers."
    num = 0
    while num < x:
        num = next(fibonacci_generator())
        if num == x:
            erase_stored_values()
            return f"Yes, {x} is a fibonacci number."
    erase_stored_values()
    return f"No, {x} is NOT a fibonacci number."

def fibonacci_this_Index_Range(lowerIndex,higherIndex):
    if fibonacci_error(lowerIndex): return "Invalid input! Input must be positive integers."
    if fibonacci_error(higherIndex): return "Invalid input! Input must be positive integers."
    fibonacci_db = {1:0,2:1}
    if lowerIndex == higherIndex or higherIndex<lowerIndex:
        return "Invalid input both numbers must de unique."
    counter, fibonacci_db = 3, {1:0, 2:1}
    if higherIndex == 1: return fibonacci_db
    for index in range(3, higherIndex+1):
        fib_num = next(fibonacci_generator())
        if index >= lowerIndex:
            fibonacci_db[index] = fib_num
    erase_stored_values()
    return fibonacci_db

def fibonacci_this_number_Range(lowerNum,higherNum):
    if fibonacci_error(lowerNum): return "Invalid input! Input must be positive integers."
    if fibonacci_error(higherNum): return "Invalid input! Input must be positive integers."
    if lowerNum == higherNum or higherNum<lowerNum:
        return "Invalid input both numbers must de unique."
    counter, fibonacci_db = 3, {1:0, 2:1}
    if higherNum == 1: return fibonacci_db
    while True:
        fib_num = next(fibonacci_generator())
        if fib_num > higherNum:
            erase_stored_values()
            return fibonacci_db
        if fib_num >= lowerNum:
            fibonacci_db[counter] = fib_num
        counter += 1

def menu():
    print("Welcome to the fibonacci solver app. Let us know which operation "
          "from the following you wish to use...")
    print("""
    1. Get a sample of the fibonacci series.
    2. Get a dictionary of fibonacci series upto a particular index.
    3. Get the ith fibonacci series.
    4. Get fibonacci series from range of index x to index y.
    5. Get fibonacci numbers occuring between x and y (not indexes but actual numbers).
    6. Check if a particular number is a fibonacci number.
    7. Get a fibonacci iterator that you can use from the second index onwards.
    """)
    try:
        selection =int(input("Type the selection. Eg. type 1 for the first option."))
        if selection <1 or selection>7:
            return "Invalid Entry"
    except:
        return "Invalid Entry."
    if selection in (2,3,6):
        #question for 1 num input
        pass
    elif selection in (4,5):
        #get double input
        pass
    elif selection == 7:
        return fibonacci_generator()
    else:
        return get_upto_ith_fibonacci(15)

def _test_code_integrity():
    print("\nInitiating testing of all functions...\n")
    print("\n\tPerformming all tests on / with no 34, a fibonacci number\n")
    print("\tTesting function: get_reusable_fibonacci\t", get_reusable_fibonacci(10))
    print("\tTesting function: get_ith_fibonacci\t\t", get_ith_fibonacci(10))
    print("\tTesting function: get_upto_ith_fibonacci\t", get_upto_ith_fibonacci(10))
    print("\tTesting function: fibonacci_checker\t\t", fibonacci_checker(34))
    print("\tTesting function: fibonacci_this_Index_Range\t", fibonacci_this_Index_Range(0, 10))
    print("\tTesting function: fibonacci_this_number_Range\t", fibonacci_this_number_Range(0, 40))
    print("\tTesting function: fibonacci_recurcive\t\t",fibonacci_recurcive(10,prints=False))






if __name__ == "__main__":
    _test_code_integrity()
    #print(menu())
else:
    print("imported fibonacci...")
