import os
import random

def word_search():
    word_list = []
    with open ("./Files/data.txt", "r", encoding="utf-8") as f:
        for line in f:
            word_list.append(line.strip())
    f.close()
    word = random.choice(word_list).upper()
    print(word)
    return word

def play(word):
    correct_words = []
    correct_letters = []
    game_status = False
    lives = 6

    blanks = "_" * len(word)

    while game_status != True and lives > 0:
        print("")
        print(hangman_stages(lives))
        for user_in in blanks:
            print(user_in, end=" ")
        print("")
        print(word)
        
        print(f"Your lives {lives}")
        print("")
        user_in = input("Guess a letter or word: ").upper()
        if len(user_in) == 1 and user_in.isalpha:
            if user_in in correct_letters:
                print("You already guessed that letter.") 
            elif user_in not in word:
                print(f"'{user_in}' is not part of the word.")
                lives -= 1
            else:
                correct_letters.append(user_in)
                print(correct_letters)
                print("Well done! You guessed a letter.")
                for i in range(len(word)):
                    if word[i] in correct_letters:
                        blanks = blanks[:i] + word[i] + blanks[i+1:]
                if set(word) == set(correct_letters):
                    game_status = True
                    #os.system('cls')
                    #win(word)
        elif len(user_in) == len(word) and user_in.isalpha:
            if user_in == word:
                game_status = True
                os.system('cls')
                win(word)
            else:
                print(f"{user_in} is not the word.")
                lives -=1
        else:
            print("Invalid input.")


    return lives

def welcome():
    print("""
                        * By Jotaherra *
-----------------------------------------------------------------
 _                                                   _______
| |                                                 |/      |   
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __       |      (_)
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \      |      \|/
| | | | (_| | | | | (_| | | | | | | (_| | | | |     |       |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|     |      / \\
                    __/ |                           |  
                   |___/                           _|___
-----------------------------------------------------------------
""")

    input("Press Enter to continue...")
    os.system('cls')

def gameover():
    print(""" 
-----------------------------------------------------------------
                    _____                          
                   / ____|                         
                  | |  __   __ _  _ __ ___    ___  
                  | | |_ | / _` || '_ ` _ \  / _ \ 
                  | |__| || (_| || | | | | ||  __/ 
                   \_____| \__,_||_| |_| |_| \___| 
                        ___ __   __ ___  _ __          
                       / _ \\\ \ / // _ \| '__|         
                      | (_) |\ V /|  __/| |            
                       \___/  \_/  \___||_| 

-----------------------------------------------------------------                                         
""")

def win(word):
    print(f"""
                   * The word was: {word} *
----------------------------------------------------------------- 
             __     __                    _       
             \ \   / /                   (_)      
              \ \_/ /__  _   _  __      ___ _ __  
               \   / _ \| | | | \ \ /\ / / | '_ \ 
                | | (_) | |_| |  \ V  V /| | | | |
                |_|\___/ \__,_|   \_/\_/ |_|_| |_|

-----------------------------------------------------------------
""")

def hangman_stages(lives):
    stages = [  # final state: head, torso, both arms, and both legs
"""
--------
|      |
|      O
|     \\|/
|      |
|     / \\
-
""",
# head, torso, both arms, and one leg
"""
--------
|      |
|      O
|     \\|/
|      |
|     / 
-
""",
# head, torso, and both arms
"""
--------
|      |
|      O
|     \\|/
|      |
|      
-
""",
# head, torso, and one arm
"""
--------
|      |
|      O
|     \\|
|      |
|     
-
""",
# head and torso
"""
--------
|      |
|      O
|      |
|      |
|     
-
""",
# head
"""
--------
|      |
|      O
|    
|      
|     
-
""",
# initial empty state
"""
--------
|      |
|      
|    
|      
|     
-
"""
    ]
    return stages[lives]

def run():
    welcome()
    word = word_search()
    play(word)

if __name__ == '__main__':
    run()