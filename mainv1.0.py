from mimetypes import init
import os
import random
import time

#Word list reader and choicer
def word_list():
    global word
    global word_split
    words = []

    with open("./Files/data.txt", "r", encoding="utf-8") as f:
        for line in f:
            words.append(line.strip())
        f.close()

    word = random.choice(words).upper()
    word_split = list(word)

def menu():
    pass;

#Main code function
def play():
    global tries
    tries = 6
    game_status = False
    correct_letters = []
    correct_words = []
    word_spaces = "_" * len(word)
#Clear the welcome
    input("Press Enter to continue...")
    os.system('cls')
#Game init
    while game_status != True and tries > 0:
        #Prints graph and spaces 
        print(hangman_graph())
        print("")
        #print(f"You have {tries} tries left.")
        print(word_spaces)
        print(correct_letters)
        print(word_split)
        

        user_in = input("Guess a letter or word: ").upper()
        #Evaluate if it is a letter
        if len(user_in) == 1 and user_in.isalpha():

            if user_in in word:
                correct_letters.append(user_in)
                print(f"Well done! You guessed the letter {user_in}.")
                quantity = word.count(user_in)
                print(f"q {quantity}")
                init = 0

                for i in range(quantity):
                    pos = word.find(user_in, init)
                    word_spaces = word_spaces[:pos] + user_in + word_spaces[init + 1:]
                    pos += 1
                
            
            elif user_in in correct_letters:
                print(f"You alreeady guessed the letter {user_in}.")

            else:
                tries -= 1
                print(f"The letter {user_in} is not in the word.")

        #Evaluate if it is the complete word
        elif len(user_in) == len(word) and user_in.isalpha():

            if user_in == word:
                correct_words.append(user_in)
                print(f"You gussed it! The word was {word}.")
                game_status = True

            else:
                print(f"{user_in} is not the word.")
                tries -= 1
        
        else:
            print("Invalid input.")


        input()
        os.system('cls')

    welcome()



#Interface function
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


def hangman_graph():
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
    return stages[tries]




#Main function
def run():
    welcome()
    menu()
    word_list()
    play()



if __name__ == '__main__':
    run()
