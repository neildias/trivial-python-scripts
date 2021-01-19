#collects 4 grades
def only_nums(x):
    for number in x:
        for digit in number:
            if digit in "0123456789":
                return True

def verify_grades(x):
    if float(x) > 0 and float(x) <= 100.00:
        return True

def acquire_grades():
    while True:
        grades = input("Please input four of your grades separated by a space bar.")
        print("You entered the following grades :{}".format(grades))
        confirmation = input("\nAre these the correct grades (only numbers will be considered)?" \
                                    " If yes, type 'y', else type any key : ")
        if confirmation == 'y' or confirmation == 'Y':
            return grades



if __name__ == "__main__":

    list_grades = acquire_grades().split(" ")

    list_grades = [grade.strip() for grade in list_grades
                  if only_nums(grade) and verify_grades(grade)]

    print(list_grades)
    while len(list_grades) != 4 :
        print("\nWrong Input!!! 4 valid grades not received. Lets try again: ")
        print("\nPlease type 4 grades separated by a single space...")
        list_grades = acquire_grades().split(" ")

    # try:
    #     new_grades = list(map(float, list_grades))
    # except:
    #     print("\nWrong Input!!! Please type 4 grades separated by a single space. Lets try again: ")
    #     list_grades = acquire_grades().split(" ")

    grades_floats = list(map(lambda x: float(x), list_grades))
    sorted_grades =  sorted(grades_floats)

    print("\nYour grades sorted from the lowest to highest is {}".format(sorted_grades))
    for i in range(2):
        #note that remove returns none, therefore do not assign
         #will remove first element
        popped = sorted_grades[::-1].pop()
        sorted_grades.remove( sorted_grades[0])
        print("Your {} lowest grade to be dropped is {}".format(
                                                    "1st" if i==0 else "2nd",
                                                                     popped))

    print(sorted_grades)
    if sorted_grades[-1] < 50:
        print("\nYou can do much better. Study harder. ")

    elif sorted_grades[-1] < 75:
        print("Your scores are okay but you must aim higher. ")

    elif sorted_grades[-1] < 90:
        print("You're grades are cool! ")

    else:
        print("You are a rock star!!! Here's a bow for scoring > 90 in one of your subjects")

    #removes the last two grades

    #comments on the highest grades
