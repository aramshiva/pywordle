
import random
import sys
import time

CLEAR = "\033[H\033[J"
def Start():
    words = open("/Users/ashiva/Code/PythonCode/Data/wordle.txt", "r")
    words = words.read().splitlines()
    word = random.choice(words)
    finalresult = []
    print("WELCOME TO WORDLE".ljust(20))
    print("BY ARAM".ljust(20))
    print()
    print("✅ means it is in the right spot".ljust(20))
    print("⬆️ means it is in the word but in the wrong spot".ljust(20))
    print("❌ means it isnt in the word".ljust(20))
    print()
    input("Press ENTER key to start!\n")
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    Won = False
    for i in range(6):
            if not Won:
                Checker = True
                while Checker:
                    guess = input("what is your guess? type Q to quit\n")
                    if guess == "Q": sys.exit()
                    if len(guess) != 5: raise Exception("The word must be 5 letters!")
                    if not guess.lower() in words: print("Not a word!")
                    else: Checker = False
                result = []
                for i in range(5):
                    if guess[i] == word[i] or guess[i].upper() == word[i].upper(): result.append('✅')
                    elif guess[i] in word or guess[i].upper() in word.upper(): result.append('⬆️')
                    else: result.append('❌')
                print(" ".join(result))
                finalresult.append(" ".join(result))
            if guess == word:
                break
    print(CLEAR)
    print("WORDLE".center(20))
    print()
    for i in finalresult: print(i)
    if guess == word: print("You guessed correct! Todays wordle was " + word.capitalize() + "\nThe wordle will change tommorrow. You can keep this tab open or come back tommorow!")
    else: print("You guessed uncorrectly! Todays wordle was " + word.capitalize() + "\nThe wordle will change tommorrow. You can keep this tab open or come back tommorow!")
def ChangeWordle():
    print("The wordle today has changed.")
    Start()
Start()
day = time.strftime('%A')
while day == time.strftime('%A'):
    day = time.strftime('%A')
    pass
ChangeWordle()