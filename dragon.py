import random
import time

def displayIntro():
    print("You are in a land full of dragons. In front of you, you see two caves. In one cave, the dragon is friendly and will share his treasure with you. In the second cave the dragon is greedy and hungry and he will eat you.")
print()

def chooseCave():
    cave= ""
    while cave !='1' and cave != '2':
        print("Which cave will you go into? (1 or 2)")
        cave= input()

        return cave
    
def checkCave(chosenCave):
        print("you approach the cave...")
        time.sleep(2)
        print("A large dragon jumps out in front of you! He opens his jaws and..")
        print()
        time.sleep(2)

        friendlyCave= random.randint(1,2)

        if chosenCave == str(friendlyCave):
            print("Gives you his treasure!")
        else:
            print("Eats you in one bite")
            
playAgain = "yes"
while playAgain == "yes" or playAgain == "y":
    displayIntro()
    caveNumber = chooseCave()
    checkCave(caveNumber)

    print("Do you want to play again? (yes or no)")
    playAgain = input()