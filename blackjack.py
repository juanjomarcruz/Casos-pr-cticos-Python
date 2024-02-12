#Programación Orientada a objetos (POO): BlackJack
import random

suits=['Spades','Clubs','Diamonds','Hearts']
ranks=['2','3','4','5','6','7','8','9','10','J','Q','K','A']
values={'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'J':10,'Q':10,'K':10,'A':11}
class Card:
  def __init__(self,suit,rank):
    self.suit=suit
    self.rank=rank
  def __str__(self):
    return self.rank + 'of' + self.suit
class Deck:
  def __init__(self):
    self.deck=[]
    for suit in suits:
      for rank in ranks:
        self.deck.append(Card(suit,rank))
  def __str__(self):
    deck_comp=''
    for card in self.deck:
      deck_comp+= '\n'+card.__str__()
    return 'The deck has' + deck_comp
  def shuffle(self):
    random.shuffle(self.deck)
  def deal(self):
    single_card=self.deck.pop()
    return single_card
class hand:
  def __init__(self):
    self.cards=[]
    self.value=0
    self.aces=0
  def add_card(self,card):
    self.cards.append(card)
    self.value+=values[card.rank]
    if card.rank=='A':
      self.aces+=1
  def adjust_for_aces(self):
    if self.value > 21 and self.aces:
      self.value-=10
      self.aces-=1
class chips:
  def __init__(self):
    self.total=100
    self.bet=0
  def win_bet(self):
    self.total+=self.bet
  def lose_bet(self):
    self.total-=self.bet

def take_bet(chips):
  while True:
    try:
      chips.bet=int(input(f'Inserte cuántas fichas deseas apostar: '))
    except ValueError:
      print('Inserte un número entero')
    else:
      if chips.bet > chips.total:
        print(f'No tienes suficientes fichas. (Actualmente tienes {chips.total}).')
      else:
        return chips

def hit(hand,deck):
  hand.add_card(deck.deal())
def hit_or_stand():
  while True