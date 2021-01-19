print("\nHello, and welcome to the miles per hour (MPH) conversion app.\n")

name = input("What shall I call you? : ")

print(f"\nHello, {name}!!! We hope you are doing well!!\n")

def get_speed():
    speed = input("What is your current working speed in MPH? ")
    try:
        return float(speed)
    except:
        print("Wrong input! Please input a valid number. Let's try again. ")
        return get_speed()


speed = get_speed()

def mph_ms(mph):
    km2m = 1000   #1km == 1000 m
    miles2km = 1.609  #miles to hour
    hr2sec = 3600   #hour to second
    return round( (mph*km2m*miles2km) / hr2sec, 2 )

print("\n\nYour speed in meter per seconds is : {}".format(mph_ms(speed)))
