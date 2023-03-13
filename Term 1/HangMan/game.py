import settings
import settings as settings
import random

def gameHangman():
    word = random.choice(settings.WORDS)
    soFar = "?"*len(word)
    usedLetters = []

    print("Welcome to Hangman. Good luck!")
    while settings.guesses < settings.maxGuess and soFar != word:
        print("You have use the following letters:")
        print(usedLetters)

        print(settings.HANGMAN[settings.guesses])

        print("\nSo far, the word is: \n", soFar)

        guess = input("\n\npick a letter: ")
        while guess in usedLetters:
            guess = input("\n\npick a letter: ")
            if guess.isalpha():
                guess = guess.upper()
            else:
                continue
        usedLetters.append(guess)

        if guess in word:
            print("\nYes!", guess, "is in the word!")
            new = ""
            for i in range(len(word)):
                if guess == word[i]:
                    new += guess
                else:
                    new += soFar[i]
            soFar = new

        else:
            print("\nSorry,", guess, "isn't in the word.")
            settings.guesses += 1

def displayIntructions():
    print("""
    Welcome to the greatest intellectual challenge of all time: Tic-Tac-Toe.
    This will be a showdown between your human brain and my silicon professor.
    """)
    print("""
    You will make your move known by entering a number, 1 - 9. The number
    will correspond to the board position as illustrated:
    """)
    displayBoard([1,2,3,4,5,6,7,8,9])
    print(" Prepare yourself, human. The ultimate battle is about to begin")
    print(" ")
    input("Press enter to continue")

def displayBoard(curboard):
    print(str.format("""
    \t{0} | {1} | {2}
    \t--+---+--
    \t{3} | {4} | {5}
    \t--+---+--
    \t{6} | {7} | {8}
    """,curboard[0],curboard[1],curboard[2],curboard[3],curboard[4],curboard[5],curboard[6],curboard[7],curboard[8]))

def firstChoice():
    choice = " "
    while (True):
        print(" ")
        choice = input("Pick a number 1 or 2 decide who goes first. If you pick 1 you go first but if you pick 2 I go first.")
        if(choice == "1"):
            print(" ")
            print("Ok you're X's you go first.")
            return choice
        elif(choice == "2"):
            print("Ok you're O's I go first... Good luck")
            return choice
        else:
            print("Not a number in range")



def newBoard():
    board = [" "," "," "," "," "," "," "," "," "]
    for i in range(settings.MAXSPOTS):
        board.append(settings.E)
    return board

def setPieces():
    choice = firstChoice()
    if choice == "1":
        human = settings.X
        comp = settings.O
    else:
        human = settings.O
        comp = settings.X
    return human,comp

def humanTurn(board):
    legal = legalMoves(board)
    choice = -1
    while choice not in legal:
        choice = settings.getNumberInRange("What square would you like?",1, settings.MAXSPOTS)-1
        if choice not in legal:
            print("\nThat square is already taken, foolish human. Choose another.\n")

    return choice

def compTurn(board,comp,human):

    copyOfBoard = board[:]
    legal = legalMoves(board)


    diff = "hard"
    if diff == "easy":

        choice = 0
        choice = random.choice(legal)
        return choice
    elif diff == "normal":

        if(comp == settings.X):
            bestMovesList = [4,0,2,6,8,1,3,5,7]
        else:
            bestMovesList = [0,2,6,3,4,5,7,6,8]

    elif diff == "hard":
        if (comp == settings.X):
                bestMovesList = [2, 5, 0, 7, 6, 1, 3, 4, 8]
        else:
                bestMovesList = [4,0,2,6,8,1,3,5,7]

    for move in legal:

        copyOfBoard[move] = comp
        if winner(copyOfBoard) == comp:
            print("I shall take square number"+str(move+1))

            return move

        copyOfBoard[move]=settings.E

    for move in legal:
        copyOfBoard[move] = human
        if winner(copyOfBoard) == human:
            print("I shall take square number"+str(move+1))
            return move

        copyOfBoard[move] = settings.E

    for move in bestMovesList:
        if move in legal:
            print("I shall take square number" + str(move + 1))
            return move







def legalMoves(board):
    moves = []
    for i in range(settings.MAXSPOTS):
        if board[i] == settings.E:
            moves.append(i)
    return moves

def winner(board):
    winner = ""
    waysToWin = [[0,1,2],[3,4,5],[6,7,8],[0,4,8],[2,4,6],[0,3,6],[1,4,7],[2,5,8]]
    for row in waysToWin:
        if board[row[0]] == board[row[1]] == board[row[2]] != settings.E:
            winner = board[row[0]]
            return winner
    if settings.E not in board:
        print("Tie")
        return "Tie"
    return None

def nextTurn(turn):

    if turn == settings.X:
        return settings.O
    else:
        return settings.X

def congrats(win,comp,human):
    if winner != "Tie":
        print(win,"has won!!!   \n")
    if win == comp:
        print(" ")
        print("As I predicted, human, I am triumphant once more.   \n"
              "Proof that computers are superior to humans in all regards.")
        print("""


                """)
    elif win == human:
        print(" ")
        print("No, No! It cannot be! Somehow you tricked me, human.  \n"
              "But never again! I, the computer, so swear it!")
        print("""


                """)
    elif win == "Tie":
        print(" ")
        print("You were most lucky, human, and somehow managed to tie me.   \n"
              "Celebrate today... for this is the best you will ever achieve.")
        print("""
        
        
        """)

def gameTictactoe():
    displayIntructions()
    board = newBoard()
    human,comp = setPieces()
    turn = settings.X
    displayBoard(board)
    while not winner(board):
        if turn == human:
            move = humanTurn(board)
            board[move]= human
        else:
            move = compTurn(board, comp, human)
            board[move] = comp
        displayBoard(board)
        turn = nextTurn(turn)
    win = winner(board)

