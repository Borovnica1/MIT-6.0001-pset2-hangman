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
    hits = 0
    for letter in secret_word:
        if letter in letters_guessed:
            hits += 1
    if hits == len(secret_word):
        return True
    else:
        return False



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    guessWord = []
    for letter in secret_word:
        if letter in letters_guessed:
            guessWord.append(letter)
        else:
            guessWord.append('_ ')
    
    return ''.join(guessWord)



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    avail_letters = ''
    for letter in string.ascii_lowercase:
        if letter not in letters_guessed:
            avail_letters += letter
    return avail_letters
            
    
def uniqLetters(secret_word):
    
    uniqLetters = []
    
    for letter in secret_word:
        if letter not in uniqLetters:
            uniqLetters.append(letter)
    return len(uniqLetters)


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
    print('Welcome to the game of hangman!')
    print('I am thinking of a word that is ', len(secret_word), ' long.')
    letters_guessed = []
    number_of_guesses = 6
    warning = 3
    guessWord = []
    vowels = ['a' , 'e', 'u', 'i', 'o']
    
    for letter in secret_word:
        guessWord.append('_ ')
    guessWord = ''.join(guessWord)
    print(guessWord)
    
    while number_of_guesses > 0:
        print('You have ', warning, ' warnings left.')
        print('You have ', number_of_guesses, ' guesses left.')
        print('Available letters: ', get_available_letters(letters_guessed))
        guess = input('Please guess a letter: ')
        guess = str.lower(guess)
        
        while warning > 0 or number_of_guesses > 0:
            if not str.isalpha(guess) or guess in letters_guessed:
                if warning == 0:
                    number_of_guesses -= 1
                    print('Please type only available letters.', 'You have ', number_of_guesses, ' guesses left!')
                elif guess in letters_guessed:
                    warning -= 1
                    print('You have already ', guess, ' guessed!', '. You have ', warning, ' warnings left!')
                else:
                    warning -= 1
                    print('Please type only letters. You have ', warning, ' warnings left!')
                guess = input('Please guess a letter: ')
                guess = str.lower(guess)
            else:
                break
            
        
        letters_guessed.append(guess)
        guessWord2 = get_guessed_word(secret_word, letters_guessed)
        if guessWord != guessWord2:
            print('Good guess: ', guessWord2)
        else:
            print('Oops! That letter is not in my word: ', guessWord)
            if guess in vowels:
                number_of_guesses -= 2
            else:
                number_of_guesses -= 1
        guessWord = guessWord2
        print('--------------------')
        if is_word_guessed(secret_word, letters_guessed):
            score = number_of_guesses * uniqLetters(secret_word)
            print('Congratulations, you won! Your total score for this game is: ', score)
            break
    if not is_word_guessed(secret_word, letters_guessed):
        print('Unfortunetely you lost. The secret word was: ', secret_word)
    
   

        



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
    word = my_word.replace(" ", "")
    wordLetters = {}
    otherWordLetters = {}
    
    if len(word) != len(other_word):
            return False
        
    for i in range(len(word)):
        
        if word[i] in wordLetters:
            wordLetters[word[i]] += 1
        else:
            wordLetters[word[i]] = 1
            
        if other_word[i] in otherWordLetters:
            otherWordLetters[other_word[i]] += 1
        else:
            otherWordLetters[other_word[i]] = 1
        
        if word[i] == '_':
            continue
        if word[i] != other_word[i]:
            return False
    print(wordLetters, otherWordLetters)
    
    for letter in wordLetters:
        if letter == '_':
            continue
        print(letter, wordLetters[letter], otherWordLetters[letter])
        
        if wordLetters[letter] != otherWordLetters[letter]:
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
    
    word = my_word.replace(" ", "")
    
    matches = []
    
    for theWord in wordlist:
        broken = False
        notValidWord = False
        
        wordLetters = {}
        otherWordLetters = {}
        if len(theWord) > len(word):
            break
        if len(theWord) != len(word):
            continue
        
        # Only the same length words are compared
        for i in range(len(word)):
            
            if word[i] in wordLetters:
                wordLetters[word[i]] += 1
            else:
                wordLetters[word[i]] = 1
                
            if theWord[i] in otherWordLetters:
                otherWordLetters[theWord[i]] += 1
            else:
                otherWordLetters[theWord[i]] = 1
            
            
            
            if word[i] == '_':
                continue
            if word[i] != theWord[i]:
                broken = True
                break
            
        if broken: continue
        
        for letter in wordLetters:
            if letter == '_':
                continue
            
            if wordLetters[letter] != otherWordLetters[letter]:
                notValidWord = True
                break
        if not notValidWord:
            matches.append(theWord)
    
    if matches == []:
        print('No matches found!')
    else:    
        print('Possible word matches are: ')
        print(' '.join(matches))
            



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
    print('Welcome to the game of hangman!')
    print('I am thinking of a word that is ', len(secret_word), ' long.')
    letters_guessed = []
    number_of_guesses = 6
    warning = 3
    guessWord = []
    vowels = ['a' , 'e', 'u', 'i', 'o']
    
    for letter in secret_word:
        guessWord.append('_ ')
    guessWord = ''.join(guessWord)
    print(guessWord)
    
    while number_of_guesses > 0:
        print('You have ', warning, ' warnings left.')
        print('You have ', number_of_guesses, ' guesses left.')
        print('Available letters: ', get_available_letters(letters_guessed))
        guess = input('Please guess a letter: ')
        guess = str.lower(guess)
        
        while warning > 0 or number_of_guesses > 0:
            if guess == '*': break
            if not str.isalpha(guess) or guess in letters_guessed:
                if warning == 0:
                    number_of_guesses -= 1
                    print('Please type only available letters.', 'You have ', number_of_guesses, ' guesses left!')
                elif guess in letters_guessed:
                    warning -= 1
                    print('You have already ', guess, ' guessed!', '. You have ', warning, ' warnings left!')
                else:
                    warning -= 1
                    print('Please type only letters. You have ', warning, ' warnings left!')
                guess = input('Please guess a letter: ')
                guess = str.lower(guess)
            else:
                break
        
        if guess == '*':
            show_possible_matches(guessWord)
            continue
            
        
        letters_guessed.append(guess)
        guessWord2 = get_guessed_word(secret_word, letters_guessed)
        if guessWord != guessWord2:
            print('Good guess: ', guessWord2)
        else:
            print('Oops! That letter is not in my word: ', guessWord)
            if guess in vowels:
                number_of_guesses -= 2
            else:
                number_of_guesses -= 1
        guessWord = guessWord2
        print('--------------------')
        if is_word_guessed(secret_word, letters_guessed):
            score = number_of_guesses * uniqLetters(secret_word)
            print('Congratulations, you won! Your total score for this game is: ', score)
            break
    if not is_word_guessed(secret_word, letters_guessed):
        print('Unfortunetely you lost. The secret word was: ', secret_word)



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    #secret_word = choose_word(wordlist)
    #hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
