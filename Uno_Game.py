import random
import time

COLORS = ('red', 'yellow', 'blue', 'green')
NUMBERS = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')
# Add action cards later

class Card:
    def __init__(self, color, number):
        self.color = color
        self.number = number
    
    def __str__(self):
        return f"{self.color} {self.number}"

class Hand:
    def __init__(self):
        self.cards = []
        self.new_hand()  # Populate the hand with cards upon initialization
    
    def add_card(self):
        self.cards.append(random_card())

    def play_card(self, card):
        self.cards.remove(card)
        return card

    def show_hand(self):
        for card in self.cards:
            print(card)  # This will call the __str__ method of the Card class
    
    def new_hand(self):
        for _ in range(7):  
            self.add_card()  
        print('Here\'s your new hand!')

def random_card():
    # Returns a random card with a color and a number
    ranColor = random.choice(COLORS)
    ranNumber = random.choice(NUMBERS)
    return Card(ranColor, ranNumber)

def main():
    newHand = Hand()
    newHand.show_hand()

if __name__ == "__main__":
    main()
