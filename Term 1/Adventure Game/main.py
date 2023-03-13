# Dylan Cowley
# 10/06/22
# Adventure Game

story = "You were knocked out and wake up inside a white room with two doors. There is also broken window... but its too high... only if I had a ladder"
room1 = "You are in a dark room with nothing and all you can see is a tunnel in the floor and another door..."
room2 ="You come out of the sink and see giant sized forks and plates as someone turns on the garbage disposal and there is a plate leading to the other sink... "
room3 =""
room4 ="You walk into a hamster cage and see a feeder to the West, a the wheel to the South, and a hamster tunnel to the North and an open cage door to the North-East..."
room5 = ""
room6 =""
room7 ="As you crawl through the tunnel you start to feel it get squisier. You see light at the end of the tunnel and turn out to be in a baby's bellybutton, "
room8 =""
room9 =""
room10 =""
roomquestion1 = "What do you do?? 1 or 2?"
roomquestion2= "What do you do?? 1 or 2?"
roomquestion3= "What do you do?? 1 or 2?"
roomquestion4= "What do you do?? 1 or 2?"
roomquestion5= "What do you do?? 1 or 2?"
roomquestion6= "What do you do?? 1 or 2?"
roomquestion7= "What do you do?? 1 or 2?"
roomquestion8= "What do you do?? 1 or 2?"
roomquestion9= "What do you do?? 1 or 2?"
question = "What do you do?"
options1 = ["walk","run","go"]
options2 = ["kick","break","hit"]
insults = "you suck"

import random


def gameLoop(story, question, choice, options1, options2):
    while True:
        print(story)
        while True:
            choice = input(question)
            if (choice in options1):
                story = "1"
                Room1()

            elif choice in options2:
                story = "2"
                Room5()





def Room1(room1,roomquestion1):
    while True:
        print(room1)
        while True:
            choice1 = input(roomquestion1)
            if (choice1 == "1"):
                Room4()

            elif choice1 == "2":
                Room7()

            else:
                insult()

def insult():
    insults = ["insult1","insult2"]
    print(random.choice(insults))


def Room2(room2,roomquestion2):
    while True:
        print(room2)
        while True:
            choice2 = input(roomquestion2)
            if (choice2 == "1"):
                Room4()

            elif choice2 == "2":
                Room7()

            else:
                insult()

def Room3(room3, roomquestion3):
    while True:
        print(room3)
        while True:
            choice3 = input(roomquestion3)
            if (choice3 == "1"):
                Room4()

            elif choice3 == "2":
                Room7()

            else:
                insult()
def Room4(room4, roomquestion4):
    while True:
        print(room4)
        while True:
            choice4 = input(roomquestion4)
            if (choice4 == "1"):
                Room6()

            elif choice4 == "2":
                Room3()

            else:
                insult()
def Room5(room5, roomquestion5):
    while True:
        print(room5)
        while True:
            choice5 = input(roomquestion5)
            if (choice5 == "1"):
                Room4()

            elif choice5 == "2":
                Room7()

            else:
                insult()
def Room6(room6, roomquestion6):
    while True:
        print(room6)
        while True:
            choice6 = input(roomquestion6)
            if (choice6 == "1"):
                Room4()

            elif choice6 == "2":
                Room7()

            else:
                insult()
def Room7():
    while True:
        print(room7)
        while True:
            choice7 = input(question)
            if (choice7 == "1"):
                Room9()

            elif choice7 == "2":
                Room8()

            else:
                insult()
def Room8():
    while True:
        print(room8)
        while True:
            choice8 = input(question)
            if (choice8 == "1"):
                Room4()

            elif choice8 == "2":
                Room7()

            else:
                insult()
def Room9():
    while True:
        print(room9)
        while True:
            choice9 = input(question)
            if (choice9 == "1"):
                Room4()

            elif choice9 == "2":
                Room7()

            else:
                insult()
def Winningroom():
    while True:
        print(room10)
        while True:
            choice = input(question)




Room1(room1, roomquestion1)