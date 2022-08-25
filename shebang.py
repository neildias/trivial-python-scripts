#! C:\Python32\python.exe

# to use only the above version in the command line type py c.py 
# and NOT python c.py, which will default to python 3.9 and not python 3.2

# to open this with any other specific python version other than 3.2 and the default
# type py -3.7 c.py

import sys
print("Python version" , sys.version_info[0],".", sys.version_info[1])


def add(num, num2):
    return num + num2

def sub(num, num2):
    return add(num, num2) - add(num2, num)

def mul(num, num2):
    return (num + sub(num, num2)) * (num - sub(num, num2))

def div(num, num2):
    num = num * mul(num, num2)
    num2 = num2 * mul(num2, num)
    if not (num or num2):
        return "Not possible"
    return num / num2

print()
print(10, 20)
print(mul(10, 20))
print(div(10, 20))
print(20, 10)
print(mul(20, 10))
print(div(20, 10))
