def count_gen(some_number):
    return some_number + 1

def tables(x):
    counter = 1
    while counter < 21:
        print(f'{x} * {counter} = {num* counter}')
        counter += 1
        if counter >20:
            break

def exp(x, counter=0):
    if counter > 20:
        return
    print(f'{x} * {count_gen(counter)} = {x ** counter}')
    return exp(x, counter = counter + 1)


if __name__ == "__main__":

    try:
        print("\nWelcome to the MATHS and EXPONENTIATION table app")
        print("\nThis app prints both tables upto the count of 20: \n")
        #int(float(string)) because simply int("23.23"), for example, gives error
        num = int(float(input("Please enter the number you wish the math and exponentiation tables for : ")))
        print(f'\n{num} math tables upto 20')
        print("-------------------------")
        tables(num)
        print(f'\n{num} exponentiation tables upto 20')
        print("-------------------------")
        exp(num)
        #run the program
    except:
        print("Wrong input! Please try again inputting only numerical values")
