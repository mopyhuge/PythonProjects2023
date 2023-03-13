guesses = 0



HANGMAN = ("""

  +--------+
  |        |
           |
           |
           |
           |
===============

""","""
  +--------+
  |        |
  0        |
           |
           |
           |
===============
""",
"""

  +--------+
  |        |
  0        |
  |        |
           |
           |
===============
""",
"""

  +--------+
  |        |
  0        |
 /|        |
           |
           |
===============

""",
"""

  +--------+
  |        |
  0        |
 /|\       |
           |
           |
===============
""",
"""

  +--------+
  |        |
  0        |
 /|\       |
 /         |
           |
===============
""",
"""

  +--------+
  |        |
  0        |
 /|\       |
 / \       |
           |
===============
""")

maxGuess = len(HANGMAN)-1

WORDS = ["DEBUG", "WINSOUND", "BREAK", "CONTINUE", "PRINT", "TUPLE", "LIST", "VARIABLE", "IMPORT",
         "CONSOLE", "TERMINAL", "SYNTHAX", "CODE", "LINE",  "FUNCTION", "TRUE", "CLASS",
         "FINALLY", "FROM", "ASSERT", "NONE", "BREAK", "AWAIT", "GLOBAL"]

MAXSPOTS = 9
X = "X"
O = "O"
E = " "

def getNumberInRange(question,min,max):
    while True:
        x = input(question)
        try:
            x = int(x)
        except:
            print("not a number")
            continue
        if x >= min and x <= max:
            return x
        else:
            print("not in Range")

def display_menu(options,question):
    print(question)
    for i in range(len(options)):
        print(str.format("\t({0}.) ------------- {1:<30}",i+1,options[i]))
    while True:
        choice = getNumberInRange(question,1,len(options))
        return choice

def game_quit():
    choice = display_menu(["Yes", "No"], "Are you sure you want to quit?")
    if choice == 1:
        print("Good by")
        input("Press Enter to Continue")
        quit()
    else:
        return
