coffee = {        #water, coffee, milk
    "expresso"  : [100,  18,   0],
    "latte"     : [200, 24, 150],
    "cappucino" : [250, 24, 100],
}

machine = {
    "coffee" : 300,
    "milk"   : 2000,
    "water"  : 3000,
}

price = {"expresso" : 45,
        "latte": 100,
        "cappucino": 85}

def check_ingredients(type_):
    '''Returns true is ingredients available, else false'''
    # since dict machine wont preserve the order in the for loop
    ingredients = ["water", "coffee", "milk"]
    
    for index, item in enumerate(ingredients):
        if not machine[item] >= coffee[type_][index]: 
            print(f'Machine out of {item}')
            return False
    return True

def make_coffee(type_):
    machine["water"]  -= coffee[type_][0]
    machine["coffee"] -= coffee[type_][1]
    machine["milk"]   -= coffee[type_][2]
    print("Enjoy your {}".format(type_))

def report():
    print(f"\nAvailable water in the machine {machine['water']} ml")
    print(f"Available coffee in the machine {machine['coffee']} gms")
    print(f"Available milk in the machine {machine['milk']} ml")
    
def get_coffee(coffee_type):
    if coffee_type==1:
        return "expresso"
    elif coffee_type==2:
        return "latte"
    elif coffee_type==3:
        return "cappucino"
    else:
    	return "\nInvalid input for coffee type\n"

machine_on = True 
while machine_on:
	print("\nThank you for using The Magic Coffee Machine.")
	ans = int(input("\nWhat do you wish to do? Choose from these options:\ntype 1 to make coffee, 2 to get report :: "))
	if ans == 1:
	    coffee_type = int(input("\nType 1 for expresson, 2 for latte, and 3 for capuccino :: "))
	    # check if ingredient
	    selection = get_coffee(coffee_type)
	    if check_ingredients(selection):
	        # collect amount
	        print(f"\nThat would be Rs. {price[selection]}")
	        payment = float(input("Pay here : "))

	        if payment < price[selection]:
	            print("Insufficient amount provided. Please collect it back.")
	        elif payment > price[selection]:
	            make_coffee(selection)
	            print(f"Please collect the change of Rs. {payment - price[selection]}")
	        else:
	            make_coffee(selection)
	elif ans == 2:
	    report()

	else:
		print("\nHave a nice day.")
		machine_on = False


