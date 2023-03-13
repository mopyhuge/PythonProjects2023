from game import *
import settings as settings


def main ():
    while True:
        choice = settings.display_menu(["Play Tic Tac Toe", "Play Hang Man", "Quit"], "What would you like to do?")

        if choice == 1:
            gameTictactoe()
        if choice == 2:
            gameHangman()
            if settings.guesses < len(settings.maxGuess):
                print("You win good job")
            else:
                print("You lose")
        if choice == 3:
            settings.game_quit()


    while True:
        gameHangman()
        if settings.guesses < len(settings.maxGuess):
            print("You win good job")
        else:
            print("You lose")

        answer = input("Do you want to play again Y/N")
        if answer.upper() == "Y":
            pass
        else:
            break

main()