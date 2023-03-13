class Base_Card():
   RANKS = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K" ]
   SUITS = ["♠", "♣", "♥", "♦"]

   def __init__(self,rank,suit):
       """Constructor this is called to Build an object from this class"""

       self.isFacedUP=False
       self.rank = rank
       self.suit = suit


   def __str__(self):
       """return a string rep of the object when printed"""
       ret = ""
       if self.isFacedUP:
           ret = str.format("""
             ----------
            |          |
            |          |
            |          |
            |          |
             ----------
             """)
       else:
           ret = "?????????"

       return ret

   def flip(self):
       """toggles the isFaceUP bool"""
       self.isFacedUP = not self.isFacedUP

   @property
   def value(self):
       if self.isFacedUP:
           return Base_Card.RANKS.index(self.rank)+1
       else:
           return 0





if __name__ == "__main__":
    print("This is not a program try importing and using the classes.")
    input("\n\nPress the enter key to exit.")