from player_file import *
from commonGameFunctions import *



class BlackJack_Deck(Base_Deck):

    def __init__(self):
        super(BlackJack_Deck, self).__init__()
        self.populate()
        self.shuffle()

    def populate(self):
        for suit in BlackJack_Card.SUITS:
            for rank in BlackJack_Card.RANKS:
                card = BlackJack_Card(rank, suit)
                self.cards.append(card)



class BlackJack_Card(Base_Card):
    ACE_VALUE = 1

    @property
    def value(self):
        if self.isFacedUP:
            val = BlackJack_Card.RANKS.index(self.rank)+1
            if val > 10:
                val = 10
        else:
            val = None

        return val

class BlackJack_Hand(Base_Hand):

    @property
    def total(self):
        for card in self.cards:
            if not card.value:
                return None

        t = 0
        for card in self.cards:
            t+=card.value

        have_ace = False
        for card in self.cards:
            if card.value == BlackJack_Card.ACE_VALUE:
                have_ace = True
        if have_ace and t<=11:
            t+=10

        return t

    def __str__(self):
        ret = Base_Hand.__str__(self)+"\n"
        ret+= self.name+"\n"
        ret+= str(self.total)
        return ret

    def is_busted(self):
        return self.total>21

    def flipHand(self):
        for card in self.cards:
            card.isFaceUp = True

class BlackJack_Player(BlackJack_Hand):
    def is_hitting(self):
        response = ask_yes_no("\n"+ self.name + ", do you want a hit? (Y/N): ")
        return response == "y"

    def lose(self):
        print(self.name, "loses")

    def push(self):
        print(self.name, "pushes")

    def win(self):
        print(self.name, "wins")

    def bust(self):
        print(self.name, "busts")
        self.lose()

class Blackjack_Dealer(BlackJack_Hand):
    def is_hitting(self):
        soft = True
        for card in self.cards:
            if card.value >=10:
                soft = False
        if self.total < 17 or (self.total == 17 and soft):
            return True
        else:
            return False


    def flip_first_Card(self):
        first_card = self.cards[0]
        first_card.flip()

class BlackJack_Game(object):


    def __init__(self,player_names):
        self.dealer = Blackjack_Dealer("Dealer")
        self.deck = BlackJack_Deck()
        self.players = []
        for name in player_names:
            self.players.append(BlackJack_Player(name))

    @property
    def still_Playing(self):
        sp = []
        for player in self.players:
            if not player.is_busted():
                sp.append(player)
        return sp

    def additional_cards(self,player):
        while not player.is_busted() and player.is_hitting():
            self.deck.deal([player])
            player.flipHand()
            print(player)
            if player.is_busted():
                player.bust()

    def play(self):
        self.deck.deal(self.players+[self.dealer],per_hand=2)
        self.dealer.flip_first_Card()

        for hand in self.players:
            hand.flipHand()

        for player in self.players:
            print(player)

        print(self.dealer)

        for player in self.players:
            print(player)
            self.additional_cards(player)

        self.dealer.flipHand()
        print(self.dealer)

        if self.still_Playing:
            self.__additional_cards(self.dealer)

        if self.dealer.is_busted():
            for player in self.still_Playing:
                player.win()

        else:
            for player in self.still_Playing:
                if player.total > self.dealer.total:
                    player.win()
                elif player.total < self.dealer.total:
                    player.lose()
                else:
                    player.push()

        for player in self.players:
            player.clear_hand()
        self.dealer.clear_hand()