# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    for sletter in secret_word:
      if sletter not in letters_guessed:
        return False
    return True



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    gword = ""
    for sletter in secret_word:
      if sletter in letters_guessed:
        gword += sletter + " " #Even easier to see
      else:
        gword += "_ "
    return gword
      


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    aletters = ""
    for letter in string.ascii_lowercase:
      if letter not in letters_guessed:
        aletters += letter + " " #Even easier to see
    return aletters



def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    num_guess = 6
    num_warning = 3
    vowels = "aeiou"
    letters_guessed = ""

    print("\nWelcome to Hangman!!!! \n")

    print("We will be playing a simpel game of hangman. \nYour job is to guess a is to guess a single letter from the alphabet every time I aks you to. \nI will be letting you know the letters you know of your progress at the beggining of the game and at the end of each round. \nBe warn, you only get 6 lives, for if you guess wrong or run out of warnings, and 3 warning for if you input something apart from a single letter of the alphabet or for if you input a repeated letter. \nIf you input a vowel wrong it will cost you 2 lives and a consonant will cost you 1 life.\n")

    print("Now let the game begin! \n")

    print("I am thinking of a word with " + str(len(secret_word)) + " letters. \n")

    # print(secret_word) #Testing

    print("Warning remaining " + str(num_warning) + "\n")

    print("Lives remaining: "  + str(num_guess) + "\n")

    while num_guess != 0:
      letter = input("Guess a letter: ")
      print("\n")
      if len(letter) == 1 and letter.isalpha():
        if letter not in letters_guessed:
          letter = str.lower(letter)
          letters_guessed += letter
          if letter in secret_word:
            print("Congrats, " + letter + " is in my secret word. \n")
          else:
            print("Sorry, " + letter + " is not in my secret word. \n")
            if letter in vowels:
              num_guess -= 2
            else:
              num_guess -= 1
        else:
          num_warning -= 1
          if num_warning == 0:
            print("You have given me a repeated letter, please try again. \nBy the way, you have run out of warning, if you input something wrong again I will be force to take lives away from you. \n")
          elif num_warning < 0:
            num_guess -= 1
            num_warning = 0
            print("You have given me a repeated letter, please try again. \nNow I will take a life away from you. \n")
          else:
            print("You have given me a repeated letter, please try again. \n")
      else:
        num_warning -= 1
        if num_warning == 0:
          print("You have given me a wrong input, please try again. \nRemember, it has to be a single letter from the alphabet. \nBy the way, you have run out of warning, if you input something wrong again I will be force to take lives away from you. \n")
        elif num_warning < 0:
          num_guess -= 1
          num_warning = 0
          print("You have given me a wrong input, please try again. \nRemember, it has to be a single letter from the alphabet. \nNow I will take a life away from you. \n")
        else:
          print("You have given me a wrong input, please try again. \nRemember, it has to be a single letter from the alphabet. \n")
      if is_word_guessed(secret_word, letters_guessed):
        print("Congrats, you have guessed the full word and defeated me. \n YOU WIN!!! :)\n")
        print("Total score: " + str(len(set(secret_word)) * num_guess) + "\n")
        break
      elif num_guess == 0:
        print("Sorry, you have run out of lives. \nYOU LOSE... :(\n")
        print("The word was: " + secret_word + "\n")
        break
      print("Current progress: " + get_guessed_word(secret_word, letters_guessed) + "\n")
      print("Letters yet to be guessed: " + get_available_letters(letters_guessed) + "\n")
      print("Warning remaining: " + str(num_warning) + "\n")
      print("Lives remaining: " + str(num_guess) + "\n")
  


# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    guess = my_word.replace(" ", "")
    if len(guess) != len(other_word):
      return False
    for i in range(len(guess)):
      if guess[i].lower() != other_word[i].lower() and guess[i] != "_":
        return False
    return True



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    str = ""
    for other_word in wordlist:
      if match_with_gaps(my_word, other_word):
        str += other_word + " "
    print("Possible Matches: " + str + "\n")





def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    num_guess = 6
    num_warning = 3
    vowels = "aeiou"
    letters_guessed = ""

    print("\nWelcome to Hangman!!!! \n")

    print("We will be playing a simpel game of hangman. \nYour job is to guess a is to guess a single letter from the alphabet every time I aks you to. \nI will be letting you know the letters you know of your progress at the beggining of the game and at the end of each round. \nBe warn, you only get 6 lives, for if you guess wrong or run out of warnings, and 3 warning for if you input something apart from a single letter of the alphabet or for if you input a repeated letter. \nIf you input a vowel wrong it will cost you 2 lives and a consonant will cost you 1 life.\n")

    print("Now let the game begin! \n")

    print("I am thinking of a word with " + str(len(secret_word)) + " letters. \n")

    # print(secret_word) #Testing

    print("Warning remaining " + str(num_warning) + "\n")

    print("Lives remaining: "  + str(num_guess) + "\n")

    while num_guess != 0:
      letter = input("Guess a letter: ")
      print("\n")
      if letter == "*":
        show_possible_matches(get_guessed_word(secret_word, letters_guessed))
      elif len(letter) == 1 and letter.isalpha():
        if letter not in letters_guessed:
          letter = str.lower(letter)
          letters_guessed += letter
          if letter in secret_word:
            print("Congrats, " + letter + " is in my secret word. \n")
          else:
            print("Sorry, " + letter + " is not in my secret word. \n")
            if letter in vowels:
              num_guess -= 2
            else:
              num_guess -= 1
        else:
          num_warning -= 1
          if num_warning == 0:
            print("You have given me a repeated letter, please try again. \nBy the way, you have run out of warning, if you input something wrong again I will be force to take lives away from you. \n")
          elif num_warning < 0:
            num_guess -= 1
            num_warning = 0
            print("You have given me a repeated letter, please try again. \nNow I will take a life away from you. \n")
          else:
            print("You have given me a repeated letter, please try again. \n")
      else:
        num_warning -= 1
        if num_warning == 0:
          print("You have given me a wrong input, please try again. \nRemember, it has to be a single letter from the alphabet. \nBy the way, you have run out of warning, if you input something wrong again I will be force to take lives away from you. \n")
        elif num_warning < 0:
          num_guess -= 1
          num_warning = 0
          print("You have given me a wrong input, please try again. \nRemember, it has to be a single letter from the alphabet. \nNow I will take a life away from you. \n")
        else:
          print("You have given me a wrong input, please try again. \nRemember, it has to be a single letter from the alphabet. \n")
      if is_word_guessed(secret_word, letters_guessed):
        print("Congrats, you have guessed the full word and defeated me. \n YOU WIN!!! :)\n")
        print("Total score: " + str(len(set(secret_word)) * num_guess) + "\n")
        break
      elif num_guess == 0:
        print("Sorry, you have run out of lives. \nYOU LOSE... :(\n")
        print("The word was: " + secret_word + "\n")
        break
      print("Current progress: " + get_guessed_word(secret_word, letters_guessed) + "\n")
      print("Letters yet to be guessed: " + get_available_letters(letters_guessed) + "\n")
      print("Warning remaining: " + str(num_warning) + "\n")
      print("Lives remaining: " + str(num_guess) + "\n")



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    secret_word = choose_word(wordlist)
    hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)