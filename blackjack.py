import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

playing = True

class Card:
    
    def __init__(self,suit,rank):
        self.suit=suit
        self.rank=rank
    
    def __str__(self):
        return self.rank+" of "+self.suit
    
class Deck:
    
    def __init__(self):
        self.deck = []  # start with an empty list
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))
                
    
    def __str__(self):
        deck_comp=" "
        for card in self.deck:
            deck_comp+="\n"+card.__str__()
        return deck_comp

    def shuffle(self):
        random.shuffle(self.deck)
        
    def deal(self):
        single_card=self.deck.pop()
        return single_card
    
class Hand:
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0   # start with zero value
        self.aces = 0    # add an attribute to keep track of aces
    
    def add_card(self,card):
        self.cards.append(card)
        if card.rank=="Ace":
            self.aces+=1
        self.value+=values[card.rank]
    
    def adjust_for_ace(self):
        while self.value>21 and self.aces>0:
            self.value-=10
            self.aces-=1
            
            
class Chips:
    
    def __init__(self):
        self.total = 100  # This can be set to a default value or supplied by a user input
        self.bet = 0
        
    def win_bet(self):
        self.total+=self.bet
    
    def lose_bet(self):
        self.total-=self.bet
        
        
def take_bet(chips):
    while True:
        try:
            chips.bet=int(input("enter the bet: "))
        except:
            print("sorry please provide an integer")
        else:
            if chips.bet>chips.total:
                print(f'you dont have enough chips.You have {chips.total}')
            else:
                break
    
        
def hit(deck,hand):
    
    hand.add_card(deck.deal())
    hand.adjust_for_ace()
    
    
def hit_or_stand(deck,hand):
    global playing  # to control an upcoming while loop
    
    while True:
        x=input('choose hit or stand?enter h or s :')
        
        if x[0].lower()=='h':
            hit(deck,hand)
            
        elif x[0].lower()=='s':
            print("player stand.Dealer's turn")
            playing=False
            
        else:
            print("sorry.I do not understand")
            continue
        
        break
    
    
def show_some(player,dealer):
    print("\n")
    print('DEALER hand:')
    print('one card hidden')
    print(dealer.cards[1])
    print('PLAYER hand')
    for card in player.cards:
        print(card)
    
def show_all(player,dealer):
    print("\n")
    print('DEALER hand:')
    for card in dealer.cards:
        print(card)
    print("\n")
    print('PLAYER hand')
    for card in player.cards:
        print(card)
        

def player_busts(player,dealer,chips):
    print("player BUST!")
    chips.lose_bet()

def player_wins(player,dealer,chips):
    print("player win!")
    chips.win_bet()

def dealer_busts(player,dealer,chips):
    print("player wins! dealer BUSTED! ")
    chips.win_bet()     
    
def dealer_wins(player,dealer,chips):
    print("dealer win!")
    chips.lose_bet()
    
def push(player,dealer):
    print("its a tie.PUSH!")
    
    

while True:
    # Print an opening statement
    print("welcome to blackjack game")

    
    # Create & shuffle the deck, deal two cards to each player
    deck = Deck()
    deck.shuffle()
    player=Hand()
    dealer=Hand()
    player.add_card(deck.deal())
    player.add_card(deck.deal())
    dealer.add_card(deck.deal())
    dealer.add_card(deck.deal())
    
        
    # Set up the Player's chips
    player_chips=Chips()
    
    
    # Prompt the Player for their bet
    take_bet(player_chips)

    
    # Show cards (but keep one dealer card hidden)
    show_some(player,dealer)

    
    while playing:  # recall this variable from our hit_or_stand function
        
        # Prompt for Player to Hit or Stand
        hit_or_stand(deck,player)
        
        # Show cards (but keep one dealer card hidden)
        show_some(player,dealer)
 
        
        # If player's hand exceeds 21, run player_busts() and break out of loop
        if player.value>21:
            player_busts(player,dealer,player_chips)
            break

    # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
    if player.value<=21:
        while dealer.value<player.value:
            hit(deck,dealer)
        # Show all cards
        show_all(player,dealer)
    
        # Run different winning scenarios
        print("\n")
        if dealer.value>21:
            dealer_busts(player,dealer,player_chips)
        elif dealer.value>player.value:
            dealer_wins(player,dealer,player_chips)
        elif dealer.value<player.value:
            player_wins(player,dealer,player_chips)
        else:
            push(player,dealer)
        
    
    # Inform Player of their chips total 
    print(f'player total chips={player_chips.total}')
    # Ask to play again
    newgame=input('play again?')
    if newgame[0].lower()=='y':
        playing=True
    else:
        print('thank you for playing')
        break
