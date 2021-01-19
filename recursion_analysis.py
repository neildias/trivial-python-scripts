# an Etude in factorial

def recursion_addition(n):
    if n < 0 : return  # breaks the recursion by wwill return None
    return n + recursion_addition(n-1)

try:
    print(recursion_additionfactorial(100))
except Exception as e:
    print(f"\nRunning function {recursion_addition.__name__}\n")
    print("Because the first function returned None and the recursiveness"
          " was trying to operate ON the last returned value ('None' at line 4 "
          " --- whatever was the last operand (in the case, addition) "
          " it gave the following error. ", e)


print("\t\t CORRECTING THE ABOVE ERROR")


def recursion_addition(n):
    if n < 0 : return 1 # breaks the recursion by wwill return None
    return n + recursion_addition(n-1)

try:
    print(recursion_addition(100))
    print("Merely putting an integer on the return that breaks the recursion "
          " makes the program work. Now what is important here is the last "
          " behavior of the operand. Use multiplication and you have a factorial"
          " calculator.")
except Exception as e:
    print(e)


def recursion_factorial(n):
    if n < 0 : return  # breaks the recursion by wwill return None
    if n == 0: return 1
    return n * recursion_factorial(n-1)

print(recursion_factorial(10))
