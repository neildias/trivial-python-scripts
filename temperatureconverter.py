def kelvin_to_fahrenheit(temp):
    '''(0K − 273.15) × 9/5 + 32 = -459.7°F'''

    return (temp - 273.15) * (9/5) + 32

def kelvin_to_celcius(temp):
    '''0K − 273.15 = -273.1°C'''

    return temp - 273.15

def fahrenheit_to_kelvin(temp):
    '''(0°F − 32) × 5/9 + 273.15 = 255.372K'''

    return (temp - 32) * (5/9) + 273.15

def fahrenheit_to_celcius(temp):
    '''(0°F − 32) × 5/9 = -17.78°C'''

    return (temp - 32) * (5/9)

def celcius_to_kelvin(temp):
    '''0°C + 273.15 = 273.15K'''

    return (temp + 273.15)

def celcius_to_fahrenheit(temp):
    '''(0°C × 9/5) + 32 = 32°F'''

    return (temp * (9/5)) + 32


def print_formater(kelvin, fahrenheit, celcius):
    kelvin, fahrenheit, celcius = round(kelvin,4), round(fahrenheit,4), round(celcius,4)
    print("The temperature in Kelvin is:\t\t{}".format(kelvin))
    print("The temperature in Celcius is:\t\t{}".format(celcius))
    print("The temperature in Fahrenheit is:\t{}".format(fahrenheit))

#--------------------------------------------

if __name__ == "__main__":

    print("\nPlease input the unit of the temperature you wish to get converted: ")

    while True:

        unit = input("For Kelvin type 'k', for Fahrenheit type 'f', for Celcius type 'c' : ")
        temp = float(input("Now type the numerical value of the temperature. Eg. for 100 F, simply type: 100.  :  "))
        if (isinstance(temp, float)) and unit in ('k', 'f', 'c'):
            break
        print("One of your input is wrong input: Let's try again.")

    if unit == 'k':
        kelvin = temp
        #converttion from kelvin
        fahrenheit = kelvin_to_fahrenheit(temp)
        celcius = kelvin_to_celcius(temp)
        print_formater(kelvin=kelvin,fahrenheit=fahrenheit, celcius=celcius)

    elif unit == 'c':
        #convertion from celcius
        celcius = temp
        fahrenheit = celcius_to_fahrenheit(temp)
        kelvin = celcius_to_kelvin(temp)
        print_formater(kelvin=kelvin,fahrenheit=fahrenheit, celcius=celcius)

    else:
        #convertion from fahrenheit
        fahrenheit = temp
        celcius = fahrenheit_to_celcius(temp)
        kelvin = fahrenheit_to_kelvin(temp)
        print_formater(kelvin=kelvin,fahrenheit=fahrenheit, celcius=celcius)
