import random

# hard - guess all letters

#ascii art
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']



def get_all_index(word, letter):
    indices = [index for index, w in enumerate(word)
              if w == letter]
    return indices


# give user a word

word_list = ["conspicuous", "incorrigible", "greyhound"]

random_word = random.choice(word_list)

display_word = ['_' for letter in random_word]

# game logic

won = False
strike = 0   # to declare loss

while not won:
    # show the word to be guessed
    print(display_word)

    # user input
    user_letter = input("Guess a letter :: ")

    # user guessed letter in word
    if user_letter in random_word:
        # get all indices of the letter in word
        letter_indices_in_random_word = get_all_index(random_word,
                                                      user_letter)

        for i in letter_indices_in_random_word:
            # check if ith index of display is "_"
            if display_word[i] == "_":
                # only if "_" then make the replacement
                display_word[i] = user_letter
                break

        else:
            # if user letter in the word
            # but letter already used in "display_word"
            # in other words the user has inputted the letter
            # more times than it actually occurs in the word
            # eg. user inputting 'e' 3 times or more for the
            # actual word "helper" in which e occurs just twice
            strike += 1
            print(f"Wrong Guess :( ")
            print(stages[-strike])

    # block for user letter not in word at all
    else:
        strike += 1
        print(f"Wrong Guess :( ")
        print(stages[-strike])

    #maximum wrong input
    if strike == 7:
        print("Maximum wrong guess limit exceeded")
        print("You lost")
        break

    elif "_" not in display_word:
        print("You WON!!!")
        break
