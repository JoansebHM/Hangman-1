import os
import random


def word_search():
    word_list = []
    with open("./Files/data.txt", "r", encoding="utf-8") as f:
        for line in f:
            word_list.append(line.strip())
    f.close()
    word = random.choice(word_list).upper()
    normalized_word = normalize(word)

    return word, normalized_word


def print_blanks(blanks):
    for i in blanks:
        print(i, end=" ")


def prompts(aux, user_in):
    if aux == 1:
        print(f"Good job {user_in} is part of the word")
        aux = 0

    elif aux == 2:
        print("You already guessed that one.")
        aux = 0

    elif aux == 3:
        print(f"{user_in} is not on the word.")
        aux = 0

    elif aux == 4:
        print("Invalid input.")


def normalize(word):
    replacements = (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
    )
    for a, b in replacements:
        word = word.replace(a, b).replace(a.upper(), b.upper())
    return word


def play(word, normalized_word):
    hint = random.choice(word)
    hint2 = random.choice(word)

    while hint == hint2:
        hint2 = random.choice(word)
    
    aux = 0
    user_in = ""
    guessed_words = []
    correct_letters = [hint]
    guessed_letters = [hint]

    game_status = False
    lives = 6
    blanks = "_" * len(word)

    if len(word) > 5:
        correct_letters.append(hint2)
        guessed_letters.append(hint2)

    for i in range(len(word)):
        if normalized_word[i] in correct_letters:
         blanks = blanks[:i] + word[i] + blanks[i+1:]


    while game_status != True and lives > 0:
        os.system('cls')

        prompts(aux, user_in)
        print(hangman_stages(lives))
        print_blanks(blanks)
        print("\n")

        print(f"The word has {len(word)} Characters")
        print("Your letters:", guessed_letters)
        print("Your words:", guessed_words)
        print(f"Your lives {lives}")
        print("")

        user_in = input("Guess a letter or word: ").upper()

        if len(user_in) == 1 and user_in.isalpha:
            if user_in in correct_letters or user_in in guessed_letters:
                aux = 2

            elif user_in not in normalized_word:
                guessed_letters.append(user_in)
                lives -= 1
                aux = 3

            else:
                correct_letters.append(user_in)
                guessed_letters.append(user_in)
                aux = 1

                for i in range(len(word)):
                    if normalized_word[i] in correct_letters:
                        blanks = blanks[:i] + word[i] + blanks[i+1:]

                if set(normalized_word) == set(correct_letters):
                    game_status = True
                    os.system('cls')
                    win(word)

        elif len(user_in) == len(word) and user_in.isalpha:
            if user_in == normalized_word:
                game_status = True
                os.system('cls')
                win(word)
            else:
                guessed_words.append(user_in)
                lives -= 1
        else:
            aux = 4

        if lives == 0:
            os.system('cls')
            gameover(word)

    return lives, blanks, aux, user_in


def welcome():
    os.system('cls')
    print(f"""
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


def gameover(word):
    print(f""" 
                       * The word was: {word} *
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
    word, normalized_word = word_search()
    play(word, normalized_word)

    while input("Do you want to play again? (Y/N)").upper() == "Y":
        word, normalized_word = word_search()
        play(word, normalized_word)



if __name__ == '__main__':
    run()
