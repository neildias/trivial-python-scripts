letter_dict = {}

get_word = input("Enter sentence and press Enter only after you are done entering it : ").lower()

for letter in get_word:
    if letter == " ":
        continue
    if letter in "0123456789":
        if letter not in letter_dict:
            letter_dict[letter] = 1
        else:
            letter_dict[letter] += 1
    else:
        if letter not in letter_dict:
            letter_dict[letter] = 1
        else:
            letter_dict[letter] += 1

print()
print(letter_dict)
