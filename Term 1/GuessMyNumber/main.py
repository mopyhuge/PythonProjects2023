# Dylan Cowley
# 9/26/22
# Guess My Number


import random


# global vars




# 1 pick a random number in given range
# get guess from user
# check if guess  == number
# if guess < number
# tell user to guess higher
# if guess > numbers
# tell user to guess lower

def checkforIntInput(question,min,max):
    """get a good number within a given range and validate the data befor it returns it"""
    number =""
    while(True):
        number = input(question)
        if(number.isdigit()) and ((int(number) >= min) and (int(number) <= max)):
            number = int(number)
            return number

        else:
            print("not a good input")






def main():
    min = 1
    max = 10
    number = 0
    guess = 0
    number = random.randint(min,max)
    trys = 3

    while True:
        diff = input("Choose your difficulty!!! Easy, Medium, or HARD!?!")
        if(diff in ["easy","Easy","e","E","1"]):
            min = 1
            max = 10
            trys = 3
            break
        elif("m" in diff.lower().strip()):
            min = 1
            max = 50
            trys = 5
            break
        elif("h" in diff.lower().strip()):
            min = 1
            max = 1000
            trys = 10
            break
        else:
            print("Not a good input")




    guess = checkforIntInput("Pick a number between " + str(min) + " and " + str(max),min,max)
    while(guess != number and trys>1):
        if(guess < number):
            print("Guess Higher")
            trys -= 1
            print("You have "+str(trys)+" trys left!!!")
        elif(guess > number):
            print("Guess Lower")
            trys -= 1
            print("You have " + str(trys) + " trys left!!!")
        guess = checkforIntInput("Pick a number between " + str(min) + " and " + str(max)+"you have "+str(trys) +" left",min,max)




    if(trys > 1):
        print("You got it great job!!!")
    else:
        print("Damn, you suck...")
        answer = input("Want to play again!? Yes or No?")
        if("n" in answer.lower()):
            playing = False






main()