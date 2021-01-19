year = int(input("Type the year you wish to check for leapness"))

def divisible(num,by):
    if num % by == 0:
        return True
    return False

# leap if divisible by 4, but not by 100 unless divisible by 400
if divisible(year, by=4) and (not divisible(year, by=100) or
                             divisible(year, by=400)):
    print(f"The year {year} a leap year")

else:
    print(f"The year {year} is not a leap year")



# --------------------------------------------------------
# using closures
def is_divisible_by(num):
    def check(by):
        if num % by == 0:
            return True
        return False
    return check

load_num_in_func = is_divisible_by(year)
divisible_by_4   = load_num_in_func(4)
divisible_by_100 = load_num_in_func(100)
divisible_by_400 = load_num_in_func(400)

# if divisible_by_4 and (not divisible_by_100 or divisible_by_400):
#     print(f"The year {year} a leap year")
#
# else:
#     print(f"The year {year} is not a leap year")
