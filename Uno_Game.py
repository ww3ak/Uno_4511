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
        self.playable = [] #refers to playable cards, reset every turn 

    def deal_initial_cards(self):
        for player in self.players:
            player.draw(self.deck, 7)

    def start_game(self):
        self.deal_initial_cards()
        self.current_card = self.deck.draw_card()
        self.discard_pile.append(self.current_card) 
        self.current_player_index = random.randrange(self.num_players)
        print(f"Starting with Player {self.players[self.current_player_index].player_id}")

        while True: #game loop
            print("-----NEW GAME-----")
            self.current_player = self.players[self.current_player_index] #sets current player

            print("-----PLAYER'S TURN-----")
            print(f"Player {self.current_player.player_id}'s turn")

            turn_ended = False #determines if players turn is over
            while not turn_ended:
                self.show_current_card() #shows current top deck card
                print(f"Player {self.current_player.player_id}, here is your hand:")
                self.current_player.show_hand()
                response = self.playable_cards()

                if (response == '0'):#player chooses to draw
                    print(f"Player {self.current_player.player_id} draws a card")
                    self.current_player.draw(self.deck, 1) #player draws
                    self.current_player.show_hand() #show player new hand

                    self.playable_cards(check_only=True)
                    if self.playable:  # If there are playable cards after drawing
                        print("You drew a playable card!")
                        response = '1'  # Set response to 'play a card'
                        11
                elif (response == '1'):#player chooses to play
                    cnt = 0
                    for card in self.playable:
                        print(f'[{cnt}]: {card}') 
                        cnt +=1


                    self.show_current_card()
                    played_card = input(f"Please choose the number of the card you would like to play.")
                    print(f'Player {self.current_player.player_id} plays a {self.playable[int(played_card)]}')

                    self.current_player.hand.remove(self.playable[int(played_card)])
                    self.discard_pile.append(self.current_card)#places it on top of discard pile
                    self.current_card = self.playable[int(played_card)]#updates current card


                    if self.check_for_winner():  # Check if the game has a winner
                        break  # End the game if there is a winner
                
                    turn_ended = True

                
                

            break
    
    def check_for_winner(self):
        for player in self.players:
            if len(player.hand) == 0:  # Player has no cards left
                print(f"Player {player.player_id} wins the game!")
                return True  # Indicates the game has a winner
        return False  # No winner yet, the game continues



    def next_player(self):
        self.current_player_index = (self.current_player_index + 1) % self.num_players

    def show_disc_pile(self):
        for card in self.discard_pile:
            print(card)
    
    def show_current_card(self):
        print("-----TOP DECK-----")
        print(f"{self.current_card}")
        print("------------------")


    def playable_cards(self, check_only=False):
        self.playable = []
        for card in self.current_player.hand:
            if card == self.current_card or card.get_color() == self.current_card.get_color() or card.get_number() == self.current_card.get_number():
                self.playable.append(card)  # Card is playable

        if not self.playable:
            if not check_only:
                x = input("No playable cards, please type '0' to draw") 
                return x
        else:
            if not check_only:
                print("-----PLAYABLE-----")
                for card in self.playable:
                    print(card)
                print('------------------')
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
