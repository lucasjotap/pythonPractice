def main():
    """Pig Latin Game, add way to vowel-starting words, 
    and ay to consonant-startings ones."""
    #Set string with vowel values
    vowels = "aeiouy"
    #Game main loop
    while True:
        #Get input from player
        word = input("Type a word here and I'll turn it into Pig latin for you.")
        if word[0] == vowels:
            pig_latin = word + 'way'
        else:
            pig_latin = word[1:] + word[0] + "ay"
        print(f'This is the Pig Latin translation of the word you typed:{pig_latin}')
        play_again = input('Do you want to play again? Press enter else press q to quit.')
        if play_again.lower()=='q':
            print('Thanks for playing.')
            break
if __name__ == main():
    main()