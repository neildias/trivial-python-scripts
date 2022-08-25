import random

# easier: guess some letters


# hard - guess all letters

# hangman ascii art
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
display_list = ["_o_s_ic_ous", "i_co__i_ible", "g__yho__d"]
random_word = random.choice(display_list)

#get index from display list to find the corresponding word in wordlist
index = display_list.index(random_word)
word_from_wordlist = word_list[index]
word_from_wordlist

display_word = [letter for letter in random_word]

# game logic
won = False
strike = 0   # to declare loss

while not won:
    # show the word to be guessed
    print(display_word)

    # user input
    user_letter = input("Guess a letter :: ")

    # user guessed letter in word
    if user_letter in word_from_wordlist:
        # get all indices of the letter in word
        letter_indices_in_random_word = get_all_index(word_from_wordlist,
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
            # give figure of hangman ascii art
            print(stages[-strike])


    # block for user letter not in word at all
    else:
        strike += 1
        print(f"Wrong Guess :( ")
        # give figure of hangman ascii art
        print(stages[-strike])

    #maximum wrong input
    if strike == 7:
        #print("Maximum wrong guess limit exceeded")
        print("You lost")
        break

    elif "_" not in display_word:
        print("You WON!!!")
        break
