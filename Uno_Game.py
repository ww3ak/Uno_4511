import random
import time

COLORS = ('red', 'yellow', 'blue', 'green')
NUMBERS = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')
# Add action cards later

class Game:
    '''
    PARAM: number of players
    '''
    def __init__(self, num_player):
        self.num_player = num_player
        self.players = []

    def new_game(self):
        player_count = 0;
        for player in self.num_player:
            player_count +=1
            self.players.append(Player(player_count))

        
class Player:
    def __init__(self, number):
        self.number = number
        self.hand = []




class Card:
    def __init__(self, color, number):
        self.color = color
        self.number = number
    
    def __str__(self):
        return f"{self.color} {self.number}"

class Hand:
    def __init__(self):
        self.cards = []
    
    def add_card(self):
        self.cards.append(random_card())

    def play_card(self, card):
        self.cards.remove(card)
        return card

    def show_hand(self):
        for card in self.cards:
            print(card)  
    
    def new_hand(self, deck):
        for _ in range(7):  
            self.add_card(deck.draw_card())  
        print('Here\'s your new hand!')

class Deck:
    def __init__(self):
        self.deck = []
        self.new_deck()
        #deck is made up of 108 cards: 25 red, 25 blue, 25 green, 25 yellow. 
        #2 each on 1-9 and 1 zero
        #2 draw +2, 2 reverse, 2 skip, 4 wild, 4 wild draw four
    def new_deck(self):
        self.deck = []
        for color in COLORS:
            for number in NUMBERS:
                # Adds two of each number for each color, except '0' which is added once
                self.deck.append(Card(color, number))
                if number != '0':
                    self.deck.append(Card(color, number))
    def show_deck(self):
        for card in self.deck:
            print(card)

    def draw_card(self):
        if len(self.deck) > 0:
            return self.deck.pop()
        else:
            print("The deck is empty!")
            return None

    def shuffel_deck(self):
        random.shuffle(self.deck)
        print(type(self.deck))
        
    
def random_card():
    # Returns a random card with a color and a number
    ranColor = random.choice(COLORS)
    ranNumber = random.choice(NUMBERS)
    return Card(ranColor, ranNumber)

def main():
    # newHand = Hand()
    # newHand.new_hand()
    # newHand.show_hand()
    # print("helo world")
    newDeck = Deck()
    # newDeck.show_deck()
    newDeck.shuffel_deck()
    # print(type(newDeck))
    newDeck.show_deck()



if __name__ == "__main__":
    main()
