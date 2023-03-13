#Dylan Cowley

artist = " "

artist = input("What is the artist's name?")
if len(artist) > 10 or len(artist) < 1:
    print("Hi")

if len(artist) <= 10 and len(artist) >= 1:
    signature = artist


    print("+--------------------+")
    print("|        |>          |")
    print("|        |\          |")
    print("|        | \         |")
    print("|        |  \        |")
    print("|        |   \       |")
    print("|        |    \      |")
    print("|  \==============/  |")
    print("|   \____________/   |")
    print("|      "+signature+"       |")
    print("+--------------------+")