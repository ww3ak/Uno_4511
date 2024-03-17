import random
import time

COLORS = ('red', 'yellow', 'blue', 'green')
NUMBERS = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')

class Game:
    def __init__(self, num_player, deck):
        self.num_player = num_player
        self.deck = deck
        self.players = []
        self.current_player =  None

    def new_game(self):
        self.deck.shuffle_deck() 
        for i in range(self.num_player):
            player = Player(i + 1)
            player.hand = Hand()  
            for _ in range(7):  
                player.hand.add_card(self.deck.draw_card())
            self.players.append(player)
    
    def start_game(self):
        discard_pile = []
        self.current_player = random.choice(self.players)
        print(f"Player {self.current_player.number} gets to draw the first card!")
        player_response = input(f"Player {self.current_player.number}, please type 'draw' to draw the first card: ")
        if player_response.lower() != 'draw':
            print("Please type 'draw' to continue!")
        else:
            draw_card = self.deck.draw_card()
            discard_pile.append(draw_card)
            self.next_player()  


    def show_disc_pile(self, pile):
        for card in pile:
            print(card)

    def next_player(self):
        current_index = self.players.index(self.current_player)
        next_index = (current_index + 1) % self.num_player   # Loop back to 0 after the last player
        self.current_player = self.players[next_index]
        print(f"Next player is Player {self.current_player.number}.")

class Player:
    def __init__(self, number):
        self.number = number
        self.hand = None

    def __str__(self):
        return f"{self.number}"

class Card:
    def __init__(self, color, number):
        self.color = color
        self.number = number
    
    def __str__(self):
        return f"{self.color} {self.number}"

class Hand:
    def __init__(self):
        self.cards = []
    
    def add_card(self, card):
        self.cards.append(card)

    def play_card(self, card):
        self.cards.remove(card)
        return card

    def show_hand(self):
        for card in self.cards:
            print(card)

class Deck:
    def __init__(self):
        self.deck = []
        self.new_deck()

    def __str__(self):
        return f"{self.deck}"

    def new_deck(self):
        self.deck = []
        for color in COLORS:
            for number in NUMBERS:
                # Adds two of each number for each color, except '0' which is added once
                self.deck.append(Card(color, number))
                if number != '0':
                    self.deck.append(Card(color, number))

    def shuffle_deck(self):
        random.shuffle(self.deck)

    def draw_card(self):
        if self.deck:
            return self.deck.pop()
        else:
            print("The deck is empty!")
            return None

def main():
    game = Game(2, Deck())
    game.new_game()
    # Show hands of all players
    # for i, player in enumerate(game.players, 1):
    #     print(f"Player {i}'s hand:")
    #     player.hand.show_hand()
    game.start_game()

if __name__ == "__main__":
    main()
