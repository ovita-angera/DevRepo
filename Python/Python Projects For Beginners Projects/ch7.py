# the blackjack project
# set up the necessary imports
from random import randint
from IPython.display import clear_output

# create a game class
class Blackjack():
    def __init__(self):
        self.deck = []
        self.suits = ('Spades', 'Hearts', 'Diamonds', 'Clubs')
        self.values = (2, 3, 4, 5, 6, 7, 8, 9 , 10, 'J', 'Q', 'K', 'A')

    def makeDeck(self):
        for suit in self.suits:
            for value in self.values:
                self.deck.append((value, suit))

    # method to pop a cardfrom the deck using a random index value
    def pullCard(self):
        return self.deck.pop(randint(0, len(self.deck) - 1))

# create a player class
class Player():
    balance = 1000
    wager = 0
    def __init__(self, name):
        self.name = name
        self.hand = []

    def setWager(self, wager):
        self.wager = wager
    
    def getWager(self):
        return self.wager
    
    # add cards to the player's hands
    def addCard(self, card):
        self.hand.append(card)

    # showing a player's hand
    # if it is not the dealer's turn then only show one of his cards, otherwise show all
    def showHand(self, dealer_start = True):
        print('\n{}'.format(self.name))
        print('=========')
        
        for i in range(len(self.hand)):
            if self.name == 'Dealer' and i == 0 and dealer_start:
                print('- of -') # hide the first card
            else:
                card = self.hand[i]
                print('{} of {}'.format(card[0], card[1]))

    # compute total of cards
    # if not dealer's turn then only give back total of second card
    def calcHand(self, dealer_start = True):
        total = 0
        aces = 0
        card_values = {1:1, 2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9, 10: 10, 'J':10, 'Q':10, 'K':10, 'A':11}

        if self.name == 'Dealer' and dealer_start:
            card = self.hand[1]
            return card_values[card[0]]
        
        for card in self.hand:
            if card[0] == 'A':
                aces += 1
            else:
                total += card_values[card[0]]

        for i in range(aces):
            if total + 11 > 21:
                total += 1
            else:
                total += 11
        return total

def main():
    while input("Play / Quit\n").lower() != 'quit':
        game = Blackjack()
        game.makeDeck()
        player = Player("Player")
        dealer = Player("Dealer")

        player.addCard(game.pullCard())
        dealer.addCard(game.pullCard())

        player.showHand()
        dealer.showHand()

        # Handling player's turn
        player_bust = False
        while input("Would you like to stay or hit?").lower() != 'stay':
            wager = float(input('How much do you wager? '))
            player.setWager(wager)
            clear_output()

            # pull card and put into player's hand
            player.addCard(game.pullCard())

            # show both hands using method
            player.showHand()
            dealer.showHand()

            # check if over 21
            if player.calcHand() > 21:
                player_bust = True
                player.balance -= wager
                print('New Balance: {}'.format(player.balance))
                print('You lose')
                break

        # Handling dealer's turn
        dealer_bust = False
        if not player_bust:
            while dealer.calcHand(False) < 17: # pass false to calculate all cards
                # pull card into the player's hand
                dealer.addCard(game.pullCard())

                # check if over 21
                if dealer.calcHand(False) > 21:
                    dealer_bust = True
                    player.balance += wager
                    print('New Balance: {}'.format(player.balance))
                    print('You win')
                    break

        # show both hands
        player.showHand()
        dealer.showHand()

        # calculate a winner
        if player_bust:
            print('You busted, better luck next time')
        elif dealer_bust:
            print('The dealer busted, you win')
        elif dealer.calcHand(False) > player.calcHand():
            print('Dealer has higher cards, you lose!')
        elif dealer.calcHand(False) < player.calcHand():
            print('You beat the dealer! Congrats!')
        else:
            print('You pushed. No one wins')

if __name__ == "__main__":
    main()