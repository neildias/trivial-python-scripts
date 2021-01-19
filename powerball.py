import random

print("----------------Welcome to Powerball-----------------")

#determine the pool size for the balls to be chosen

print("""

Here are the rules of:
Five white balls and 1 red ball is chosen from a pool of upto 69 no. white balls
and 26 no. red balls.

This Powerball is unique in that YOU get to choose the pool size. The larger the
pool size, the lower yours odds of winning.

For example: if you choose the poolsize for white balls as 10, and for red balls, 5:
this would mean that 10 while balls 5 balls will be chosen, and from 5 red balls
1 will be chosen.

Likewise if you choose the poolsize to be the full quota of 69 for the white balls
and 26 for the red balls - this would be out of 69 white balls 5 will be chosen
and out of 26 red balls 1 will be chosen - hence lowering the odds.\n""")

whiteWrong, redWrong = True, True

while whiteWrong:
    white_balls = int(input("Choose the poolsize to select 5 white balls from (normally max 69) : "))
    if white_balls>4:
        whiteWrong=False

while  redWrong:
    red_balls = int(input("\nChoose the poolsize to select 1 red ball from (normally max 26) : "))
    if red_balls>0and red_balls<27:
        if red_balls==1: red_balls = 2 #for the purpose of random.choice operation
        redWrong=False

def odds():
    num = red_balls
    for i in range(5):
        print(white_balls-i)
        num = num * (white_balls-i)
    return num / 120


def _no_generator():
    nums = []
    while len(nums) < 6:

        rand = random.choice(range(1, white_balls))

        #no replacement allowed as this is the white ball
        if rand not in nums:
            nums.append(rand)
            if len(nums) == 5:
                rand = random.choice(range(1,red_balls))
                #repetition allowed as this is a different ball
                nums.append(rand)
                break
    return nums

winningumbers = _no_generator()
print(f'Winning numbers are {winningumbers} \n\n')

print(f'The odds of winning this lottery are 1 in {round(odds())},0)')

ticket_nos = int(input("\nHow many tickets do you want to purchase? : "))

print("Here are your tickets: ")
counter = 0
lost=True
while counter < ticket_nos:
#for i in range(ticket_nos):
    counter += 1
    ticket = _no_generator()
    print(ticket)
    if ticket == winningumbers:
        print('congratulations: you WON!!!')
        print(f"It took you {counter} tickets to win")
        lost=False
        break
    if counter == ticket_nos-1:
        print("Do you want to buy another 1000 tickets? ")
        ask = input()
        if ask == 'y':
            ticket_nos += 1000

if lost:
    print(f"You have sadly won nothing despite buying {counter} tickets")