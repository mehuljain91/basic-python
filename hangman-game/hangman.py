# import modules

import random
import string

# list of words

words = ["january","difficult","image","film","promise","kids","lungs","doll","rhyme","damage"
                   ,"plants", "medium", "hard", "common", "smart", "real", "company", "galaxy", "star", "alone", "value", "member", "system", "table", "board", "comment", "holiday"]

# get word from list

def get_word(words):
    # random word from list
    word = random.choice(words)  
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()

def hangman():
    word = get_word(words)
    word_letters = set(word)  
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  
    
    # 7 lives
    lives = 7

    while len(word_letters) > 0 and lives > 0:
    
        print('You have', lives, 'lives left and you have used these letters: ', ' '.join(used_letters))

        word_list = [letter if letter in used_letters else '-' for letter in word]
        
        print('Current word: ', ' '.join(word_list))

        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print('')

            else:
                lives = lives - 1  
                print('\nYour letter,', user_letter, 'is not in the word.')
                if lives == 6:
                    print("""
                        ___________
                        |         
                        |        
                        |          
                        |          
                        |
                    """)
                if lives == 5:
                    print("""
                        ___________
                        | /        
                        |/        
                        |          
                        |          
                        |
                    """)
                if lives == 4:
                    print("""
                        ___________
                        | /       | 
                        |/       
                        |          
                        |          
                        |
                    """)
                if lives == 3:
                    print("""
                        ___________
                        | /       | 
                        |/       ( )
                        |          
                        |          
                        |
                    """)
                if lives == 2:
                    print("""
                        ___________
                        | /       | 
                        |/       ( )
                        |         | 
                        |         
                        |
                    """)
                if lives == 1:
                    print("""
                        ___________
                        | /       | 
                        |/       ( )
                        |         | 
                        |        / 
                        |
                    """)
        
        # if already used letter
        elif user_letter in used_letters:
            print('\nYou have already used that letter. Guess another letter.')

        else:
            print('\nThat is not a valid letter.')

    # gets here when len(word_letters) == 0 OR when lives == 0
    if lives == 0:
        print("""
            ___________
            | /       | 
            |/       ( )
            |         |
            |        / \\
            |
        """)
        print('You are hanged, sorry. The word was', word)
        play_loop()
    else:
        print('You guessed the word', word)
        play_loop()

# when game ends, playing loop

def play_loop():
    play_game = input("Do You want to play again? y = yes, n = no \n")
    while play_game not in ["y", "n","Y","N"]:
        play_game = input("Do You want to play again? y = yes, n = no \n")
    if play_game == "y":
        hangman()   
    elif play_game == "n":
        print("Thanks For Playing !!")
        exit()

hangman()
