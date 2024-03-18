import random
import time

COLORS = ('red', 'yellow', 'blue', 'green')
NUMBERS = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')

class Game:
    def __init__(self, num_players):
        self.num_players = num_players
        self.players = [Player(i + 1) for i in range(num_players)]
        self.deck = Deck()
        self.deck.shuffle_deck()
        self.discard_pile = []
        self.current_player_index = 0
        self.current_card = None #refers to current card on top of discard pile 
        self.current_player = None #self.players[self.current_player_index]

    def deal_initial_cards(self):
        for player in self.players:
            player.draw(self.deck, 7)

    def start_game(self):
        self.deal_initial_cards()
        self.current_card = self.deck.draw_card()
        self.discard_pile.append(self.current_card) 
        self.current_player_index = random.randrange(self.num_players)
        print(f"Starting with Player {self.players[self.current_player_index].player_id}")

        while True: 
            self.current_player = self.players[self.current_player_index]
            print(f"Player {self.current_player.player_id}'s turn")
            self.show_current_card()
            # print(f"Player {self.current_player.player_id}, here is your hand:")
            # self.current_player.show_hand()
            response = self.playable_cards()
            if (response == '0'):
                self.current_player.hand.append(self.current_player.draw(self.deck, 1))
                self.current_player.show_hand()
                #not sure why its printing a none at the end.fix pls
                
                

            break

    def next_player(self):
        self.current_player_index = (self.current_player_index + 1) % self.num_players

    def show_disc_pile(self):
        for card in self.discard_pile:
            print(card)
    
    def show_current_card(self):
        print(f"TOP DECK: {self.current_card}")

    def playable_cards(self):
        playable = []
        # for card in self.current_player.hand:
        #     if (card == self.current_card):
        #         playable.append(card) #same card 
        #     elif (card.get_color() == self.current_card.get_color()):
        #         # print(card.get_color())
        #         playable.append(card) #matches color
        #     elif (card.get_number() == self.current_card.get_number()):
        #         # print(card.get_number())
        #         playable.append(card) #matches number

        if not playable:
            x = input("No playable cards, please type '0' to draw") 
            return x   
        else:
            for card in playable:
                print(f'Here are your playable cards {card}')
                x = input("Would you like to play a card or draw? 1 for play and 0 for draw")
                return x 

    

class Player:
    def __init__(self, player_id):
        self.player_id = player_id
        self.hand = []

    def draw(self, deck, count=1):
        for _ in range(count):
            card = deck.draw_card()
            if card:
                self.hand.append(card)
            else:
                break  # Break if the deck is empty

    def show_hand(self):
        for card in self.hand:
            print(card)


class Card:
    def __init__(self, color, number):
        self.color = color
        self.number = number
    
    def __str__(self):
        return f"{self.color} {self.number}"
    
    def get_number(self):
        return self.number
    
    def get_color(self):
        return self.color

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
    game = Game(2)
    # Show hands of all players
    # for i, player in enumerate(game.players, 1):
    #     print(f"Player {i}'s hand:")
    #     player.hand.show_hand()
    game.start_game()

if __name__ == "__main__":
    main()
