# This imports the random module.
import random

# This is the list of the correct player guesses.
player_correct_guesses = []
# This is the list for the current player incorrect guesses.
player_incorrect_guesses = []
# This is the list of words used in the project.
list_of_words = [
    'abruptly', 'absurd', 'affix', 'askew', 'bagpipes', 'bandwagon', 'banjo', 'buffalo', 'faking',
    'fishhook', 'frazzled', 'fuchsia', 'jackpot', 'jockey', 'jukebox', 'jumbo', 'haiku', 'hungry',
    'heinous', 'hyphen', 'haphazard', 'galaxy', 'gizmo', 'glowworm', 'ginger', 'grateful'

]
# This capitalizes the entire word by looping through each letter in the word (position,) and capitalizing it.
for i in range(len(list_of_words)):
    list_of_words[i] = list_of_words[i].upper()
# This chooses a random word from my list, and uses that.
var_word = random.choice(list_of_words)
# This makes each letter its own item in the list.
list_letters_in_word = list(var_word)
# This is a dictionary that will contain the value of each letter.
value_of_letters = {}
# This looks over each letter in var_word as a for loop.
for i in var_word:
    # This adds a value to a letter if it has already been in the list, such as e in never having a value of 2 because
    # there are 2 es.
    if i in value_of_letters:
        value_of_letters[i] = value_of_letters[i] + 1
    # This adds the letter to the dictionary if it isn't in the dictionary.
    else:
        value_of_letters[i] = 1
# This is used for the losing condition for the user, which will be seen later.
user_incorrect = 0
# This is used for the winning condition for the user, which will be seen later.
user_correct = 0
print('Welcome to Hangman. If you want to play, type start.')

user_input = input()
if user_input == 'Start' or 'Start'.lower():
    # This means if the user's input isn't quit, this then plays out the program until the user inputs quit.
    while user_input != 'Quit':
        print('-----------------------------------------------------------------')
        # The maximum number of incorrect guesses a user can make is 6, the 7th triggers the game over condition.
        # Each if/elif statement prints a different body part for the person, every incorrect guess will add a new body
        # part.
        if user_incorrect == 1:
            print(' o ')
        elif user_incorrect == 2:
            print(' o ')
            print(' | ')
        elif user_incorrect == 3:
            print(' o ')
            print(' | ')
            print("/  ")
        elif user_incorrect == 4:
            print(' o ')
            print(' | ')
            print("/ \ ")
        elif user_incorrect == 5:
            print(' o ')
            print(' | ')
            print("/ \ ")
        elif user_incorrect == 6:
            print(' o ')
            print('/| ')
            print("/ \ ")
        elif user_incorrect == 7:
            print(' o ')
            print('/|\ ')
            print("/ \ ")
            print('You have used all your guesses, the word is', var_word + '.')
            print('GAME OVER')
            quit()
        # This creates a list of underscores for every letter in var_word, if the letter is in player_correct_guesses
        # this replaces the underscore with the letter instead.
        current_word_list = [letter if letter in player_correct_guesses else '_' for letter in var_word]
        # This prints the current word, which uses the list above, the join feature adds the current_word_list. This
        # naturally also shows the player's correct guesses and gives them context for the word.
        print('Current Word: ', ' '.join(current_word_list))
        # This prints the incorrect guesses so the player knows what they have already used that is incorrect.
        print('Your incorrect guesses:', player_incorrect_guesses)
        # The player's input.
        user_input = input('Guess a letter:\n')
        # This is the win condition, if the value of the players guesses is equal to the value of the word (which would
        # be the length of the word) then they win.
        if user_correct == len(var_word):
            print('You have won! Great job!')
            quit()
        if user_input.upper() in value_of_letters:
                # This is just incase the user tries to use a guess they have already used before.
                if user_input.upper() not in player_correct_guesses:
                    print('Correct!')
                    # This adds the correct guess to the list so the else statement in this if else statement works.
                    player_correct_guesses.append(user_input.upper())
                    # This adds the value of the user's input according to the dictionary to the player's score. Since
                    # each letter has its own value depending on how many times it shows up, we have to make the code
                    # reflect those different values.
                    user_correct = user_correct + value_of_letters[user_input.upper()]
                else:
                    # This makes it so the player can't spam the same input and continually get points, they have to
                    # guess each letter.
                    print('You have already guessed', user_input + ',', 'please try again')
        # This is to restrict the amount of letters the player can put, for balancing reasons.
        elif len(user_input) > 1:
            print("You can't write anything longer than a single letter!")
        # This is just incase the user tries to use an incorrect guess.
        elif user_input.upper() in player_incorrect_guesses:
            print('You have already guessed', user_input.upper() + ',', 'please try again.')
        # This adds any incorrect guess to the list, regardless of it being either a letter, or a symbol, or a blank
        # space.
        else:
            print('Incorrect guess!')
            # This is what makes the if statement way earlier that depicts the hangman work.
            user_incorrect = user_incorrect + 1
            # This appends the incorrect guess to the list so the user knows the incorrect guesses they made, and that
            # they can't make new incorrect guesses.
            player_incorrect_guesses.append(user_input.upper())
