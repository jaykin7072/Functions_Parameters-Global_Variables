#Dice roll program.
#Describe the purpose of this program here.

import random,time

s1 = "- - - - -\n|       |\n|   O   |\n|       |\n- - - - -\n"
s2 = "- - - - -\n| O     |\n|       |\n|     O |\n- - - - -\n"
s3 = "- - - - -\n| O     |\n|   O   |\n|     O |\n- - - - -\n" # All the dice states
s4 = "- - - - -\n| O   O |\n|       |\n| O   O |\n- - - - -\n"
s5 = "- - - - -\n| O   O |\n|   O   |\n| O   O |\n- - - - -\n"
s6 = "- - - - -\n| O   O |\n| O   O |\n| O   O |\n- - - - -\n"

def rollDice():
    print("Rolling.....")
    roll = random.randint(1,6) #Generate random number
    return roll


def show_dice(roll):
    if roll == 1:
        print(s1)
    elif roll == 2:
        print(s2)
    elif roll == 3:
        print(s3)
    elif roll == 4: #checking roll, printing correct state
        print(s4)
    elif roll == 5:
        print(s5)
    elif roll == 6:
        print(s6)
    else:
        print("Something is wrong with this code.")
        print(roll) #Small debug tool

def twoInRow():
    howManyRolls=int(input("How many times would you like to roll? > "))
    prevRoll="0"
    for x in range(howManyRolls):
        myRoll=rollDice()
        time.sleep(1)
        show_dice(myRoll)
        #print(myRoll) #debug
        if prevRoll==myRoll:
            print("You win life. Grats.")
            break
        prevRoll=myRoll

def whenSix():
    howManyRolls=int(input("How many times would you like to roll? > "))
    prevRoll="0"
    for x in range(howManyRolls):
        myRoll=rollDice()
        time.sleep(1)
        show_dice(myRoll)
        #print(myRoll) #debug
        if myRoll==6:
            print("You win life. Grats")
            break

whichGame=str(input("Would you like it to stop at 2 in a row (t), \nOr when you get a six (s)? > "))
if whichGame=="t":
    twoInRow() #Main program. No real point having it in a function.
elif whichGame=="s":
    whenSix()   


    

#All of the elses except the last one needed to be elif and they all needed
#== and : at the end. The show_dice function was the most buggy.
