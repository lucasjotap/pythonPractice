#Select secret word
secret_word = "love"
#List to store the failed guesses
incorrect_letter = []
#List to store the correct letters
guessed_letters = []
#Store body parts to have a guess count of n 5
body_parts = ['head', 'rlight', 'lleg', 'rarm', 'larm', 'body']
#Take player's input
guess = input("Select a letter from the alphabet: ")

if len(guess) != 1 or guess.isnumeric():
    print("Guesses can only be letters and a single one at a time.")
    guess = (input('Select a new letter for your guess: '))
    # Check if the letter guessed is not wrong
    if guess in incorrect_letter or guessed_letters:
        print(f"You've already guessed the letter{guess}\n")
        guess = (input('Select a new letter for your guess: '))

# Check if the word was guessed
if ''.join(guessed_letters) != secret_word.lower():
    guessed = False
    while guessed == False:
        # If the letter is in the secret word
        if guess in secret_word:
            # Store the correct guess in the list
            guessed_letters.append(guess)
            print("You've guessed a correct letter :D")
            guess = input("Select a new letter from the alphabet: ")
            print(guessed_letters)
            if ''.join(guessed_letters) == secret_word:
                print(guessed_letters)
                guessed = True
            
        #Else take a body part
        else:
            if len(body_parts) != 0:
                body_parts.remove(body_parts[0])
            
                #Check if the player has lost all body parts
                #Add to incorrect letters list
                incorrect_letter.append(guess)
                guess = input("Wrong guess! Select a new letter from the alphabet: ")
            else:
                print("You've run out of attempts. Game over.")
                break
    # If first condition fails the word was guessed
else:
    guessed = True
    print("You guessed the word and won the game.")
