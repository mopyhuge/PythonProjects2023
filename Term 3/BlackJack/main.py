from BlackJack_Classes import *
from card_files import *
from player_file import *
import random


def main():
    print("\t\tWelcome to BlackJack!\n")
    names = []
    num = ask_number("How many players are playing? (1 to 7)", low = 1, high = 8)
    for i in range(num):
        name =  input("Player"+str(i+1)+" enter your name")
        names.append(name)


    game = BlackJack_Game(names)
    play = None
    while play != "n":
        game.play()
        play = ask_yes_no("\nDo you want to play again?")



main()
