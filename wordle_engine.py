
import random
import sys
import time
import bold

class Styling:
    clear = "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
def Start():
    finalresult = []
    words = open("wordle.txt", "r") # Please install wordle.txt (14000 lines. A 2500 TechSmart Edition is also possible)
    words = words.read().splitlines()
    class TimeChecker:  # Classes are new
        current_day = time.strftime('%A') # They can hold data or functions and are called for by ClassName.var or ClassName.func
    word = random.choice(words)
    bold.boldprint("WELCOME TO WORDLE".ljust(20))
    print("BY ARAM".ljust(20))
    print()
    print("✅ means it is in the right spot".ljust(20))
    print("⬆️ means it is in the word but in the wrong spot".ljust(20))
    print("❌ means it isnt in the word".ljust(20))
    print()
    input("Press ENTER key to start!\n")
    print(Styling.clear)
    #print("Todays wordle is " + word + ".") #  Can be used for testing purposes
    Won = False
    for i in range(6):
            if not Won:
                guess = input("what is your guess? type Q to quit\n")
                if guess == "Q":
                    sys.exit()
                if len(guess) != 5:
                    print("The word was " + word)
                    raise Exception("The word must be 5 letters!")
                result = []
                GuessCorrect = False
                for i in range(5):
                    if guess[i] == word[i] or guess[i].upper() == word[i].upper():
                        result.append('✅')
                    elif guess[i] in word or guess[i].upper() in word.upper():
                        result.append('⬆️')
                    else:
                        result.append('❌')
                print(" ".join(result))
                finalresult.append(" ".join(result))
            if guess == word:
                break
    print(Styling.clear)
    print("WORDLE".center(20))
    print()
    for i in finalresult:
        print(i)
    if guess == word:
        print("Congrats! You guessed correct! Todays wordle was " + word.capitalize())
        while TimeChecker.current_day == time.strftime('%A'):
            pass
    else:
        bold.boldprint("You guessed uncorrectly! Todays wordle was " + word.capitalize())
        print("The wordle will change tommorrow. You can keep this tab open or come back tommorow!")
        while TimeChecker.current_day == time.strftime('%A'):
            pass
    while TimeChecker.current_day == time.strftime('%A'):
        pass
def ChangeWordle():
    print("The wordle today has changed.")
    word = random.choice(WordleStarter.words)
Start()