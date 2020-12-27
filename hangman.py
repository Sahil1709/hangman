import random

def draw_hangman(chances):
        if chances == 8:
            print("-----")
        elif chances == 7:
            print("-----")
            print("  O  ")
        elif chances == 6:
            print("-----")
            print("  O  ")
            print("  |  ")
        elif chances == 5:
            print("-----")
            print("  O  ")
            print("  |  ")
            print(" /   ")
        elif chances == 4:
            print("-----")
            print("  O  ")
            print("  |  ")
            print(" / \ ")
        elif chances == 3:
            print("-----")
            print(" \O  ")
            print("  |  ")
            print(" / \ ")
        elif chances == 2:
            print("-----")
            print(" \O/ ")
            print("  |  ")
            print(" / \ ")
        elif chances == 1:
            print("-------")
            print(" \O/__|")
            print("  |  ")
            print(" / \ ")
        else:
            print("Wrong parameter passed")    

wordlist = ["sahil","lunch","diner","thor","hangman"]
length = len(wordlist)
randomIndex = random.randint(0,length-1)
chances = 9
userWordLength = 0
previousChar = ''
while chances>0:
    currentWord = wordlist[randomIndex]
    userInput = input("Enter a char ")
    if userInput == previousChar:
        print("u cant enter same char twice")
        chances -= 1
        print(f"you have {chances} chances left.")
        draw_hangman(chances)
    else:
        for letter in currentWord:
            if userInput == letter:
                previousChar = userInput
                print(f"{userInput} <- this letter is present")
                userWordLength += 1
                if userWordLength == len(currentWord):
                    print("Congrats ! YOU WON")
                    exit()
                break
        else:
            chances -= 1
            print(f"you have {chances} chances left.")
            draw_hangman(chances)
            
print("-------")
print("  O__|")
print(" /|\  ")
print(" / \   ")
print("Hangman died")
    