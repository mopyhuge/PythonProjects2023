import string
import random

# Main game Loop
def game():

    #Make the Cards
    def make_cards():

        cards = []
        suits = ["◆", "♥", "♠", "♣"]

        for suit in suits:
            for i in range(2, 11):

                card_id = str(i) + suit

                if i == 10:

                    cards.append(card_id +  " " + card_id + "\n\n" " tony " "\n\n" + card_id + " " + card_id + "\n" )

                else:
                    cards.append( card_id +  "   " + card_id + "\n\n" " tony " "\n\n" + card_id + "   " + card_id + "\n" )

        for suit in suits:
            for i in ["J","Q","K","A"]:
                card_id = i + suit
                cards.append( card_id +  "   " + card_id + "\n\n" + " tony " "\n\n" + card_id + "   " + card_id + "\n" )


        return cards

    cards = make_cards()

    # Distribute the cards

    def play_cards(cards):

        card_shuffle = [random.choice(cards) for i in cards]
        play_cards.p1 = card_shuffle[0:26]
        play_cards.p2 = card_shuffle[26:52]

        return play_cards.p1, play_cards.p2

    play_cards(cards)


    # Show cards in game
    def card_dump(input, p1, p2):

        if input == "":
            win_add()

            return (
                    print(game_logic()),
                    print("\n"),
                    print(" __________________________________"),
                    print("|        WIN COUNTER DELUXE        |"),
                    print("".join(win_add.p1)),
                    print("|__________________________________|"),
                    print("\n"),
                    print("          Player One Card\n"),
                    print(p1[0]),
                    print("\n"),
                    print(" __________________________________"),
                    print("|        WIN COUNTER DELUXE        |"),
                    print("".join(win_add.p2)),
                    print("|__________________________________|"),
                    print("\n"),
                    print("          Player Two Card\n"),
                    print(p2[0]),
                    play_cards.p1.pop(0),
                    play_cards.p2.pop(0)
                )

    who_won = []

    # Game logic

    def game_logic():

        p1 = play_cards.p1[0][:1]
        p2 = play_cards.p2[0][:1]

        letter_value = {"A": 13, "K":12, "Q":11, "J":10}


        if p1 == "1":
            p1 = "10"
        if p2 == "1":
            p2 = "10"


        if p1 == p2:
            who_won.append(0)


        elif p1.isdigit() == True and p2.isdigit() == True:

            if int(p1) > int(p2):
                who_won.append(1)
            else:
                who_won.append(2)

        elif p1.isdigit() == False and p2.isdigit() == False:

            if letter_value[p1] > letter_value[p2]:
                who_won.append(1)
            else:
                who_won.append(2)


        elif p1.isdigit() == True and p2.isdigit() == False:

            if int(p1) > int(letter_value[p2]):
                who_won.append(1)
            else:
                who_won.append(2)

        elif p1.isdigit() == False and p2.isdigit() == True:

            if int(p2) > int(letter_value[p1]):
                who_won.append(2)
            else:
                who_won.append(1)

        return ""


    game_logic()

    # Return the list of how many times each player won

    def end_game():

        return who_won
    # Game score board "Win Counter Deluxe"
    def win_add():

        win_add.p1 = []
        win_add.p2 = []

        for i in who_won:

            if 1 == i:
                win_add.p1.append( " |")

            elif 2 == i:
                win_add.p2.append(" |")

        return win_add.p1, win_add.p2

    # Outcome Loop
    p1 = play_cards.p1
    p2 = play_cards.p2

    x = end_game()

    count = 0

    while True:

        if count == 26:

            p1_won = x.count(1)
            p2_won = x.count(2)
            draws = x.count(0)

            if p1_won == p2_won:
                print(f"The game finished in a DRAW. {p1_won} VS {p2_won}")
                break

            elif p1_won > p2_won:
                print(f"Player // ONE // won the game with {p1_won} wins VS {p2_won} for player // TWO //. There were {draws} draws.")
                break

            else:
                print(f"Player // TWO // won the game with {p2_won} wins VS {p1_won} wins for player // ONE //. There were {draws} draws.")
                break
        card_dump(input("Please hit enter"),p1, p2)
        count += 1



def main():
    game()
    while "y" in input("Play again? [Y/n]").lower():
        game()

if __name__ == '__main__':
    main()