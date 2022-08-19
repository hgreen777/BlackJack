import time
import random

def al_menu():
  print("\nWelcome to Black Jack!\n\t\tOptions\n\t'p' Play Game\n\t'h' How to play\n\t'q' Quit Game")

def all_menu():
  def choices():
    global selection
    valid_option = ['p','h','q']
    while True:
      selection = input("Please print your selection: ")
      if selection in valid_option:
        break
      else:
        print("That is not a valid option")
  choices()

  if selection == 'p':
    print("Game Starting.")
    time.sleep(1)
    print("Game Starting..")
    time.sleep(1)
    print("Game Starting...")

  if selection == 'h':
    print("\n\t\tHow to play!\n\t'c' for Card Values\n\t'i' for Game instructions\n\t'b' for Back to main menu")
    
    def instruction_Selections():
      if instruction_selection == 'c':
        print("Card Values\nA = 1 or 11\n2 = 2\n3 = 3\n4 = 4\n5 = 5\n6 = 6\n7 = 7\n8 = 8\n9 = 9\n10 = 10\nJ = 10\nQ = 10\nK = 10")
        print("\n\t\tHow to play!\n\t'c' for Card Values\n\t'i' for Game instructions\n\t'b' for Back to main menu")
        run_instructions()
  
      if instruction_selection == 'i':
        print("\n\tHow to play Black Jack\nYou will be given 2 cards")
        time.sleep(1)
        print("\nThe aim of the game is to get as close to 21 as you can with your cards") 
        time.sleep(2) 
        print("\nYou can either hit or stick \nIf you hit you will be given an extra card") 
        time.sleep(2) 
        print("\nIf you stick you will stop playing with your available cards")
        time.sleep(2) 
        print("\nOnce everyone has stuck all cards will be revealed and the closest person to 21 wins")  
        time.sleep(2)
        print("\nIf your cards evaluate to over 21 you go bust and you are out, your  cards are revealed")
        print("\n\t\tHow to play!\n\t'c' for Card Values\n\t'i' for Game instructions\n\t'b' for Back to main menu")
        run_instructions()

      if instruction_selection == 'b':
        run_all()

    
    def instruction_choices():
      global instruction_selection
      instruction_option = ['c','i','b']
      while True:
        instruction_selection = input("Please print your selection: ")
        if instruction_selection in instruction_option:
          break
        else:
          print("That is not a valid option")

    def run_instructions():
      instruction_choices()
      instruction_Selections()

    run_instructions()

  if selection == 'q':
    print("Game Closing!\nThank you for playing!\nGame made by @MrComputerized7 (Harrison)\nFollow @MrComputerized7 on twitch and Youtube")
    exit()

#Break
#Break
#Break
#Main_Game code under it
#
#

def main_game():
  math_hand = []
  player_hand = []
  dealers_hand = []

  def dealers_cards():
    global dealer_card
    for i in range(2):
      dealer_card = random.randint(1,13)
      dealers_hand.append(dealer_card)
  
    while sum(dealers_hand) < 17:
      dealers_card = random.randint(1,10)
      dealers_hand.append(dealers_card)

  def cars():
    global card
    card = random.randint(1,13)

    if card == 1:
      player_hand.append('A')
      math_hand.append(card)
    elif card == 11:
      player_hand.append('J')
      math_hand.append(10)
    elif card == 12:
      player_hand.append('Q')
      math_hand.append(10)  
    elif card == 13:
      player_hand.append('K')
      math_hand.append(10)
    else:
      math_hand.append(card)
      player_hand.append(card)

  for i in range(2):
    cars()

  dealers_cards()

  print("This is your hand {0} it totalls {1}".format(player_hand,sum(math_hand)))

  print(sum(dealers_hand))

  print("*****It is your move!*****\n\t\t'h' to hit\n\t\t's' to stick")

  def options():
    global card_selection

    def card_choices():
      
      global card_selection
      
      card_option = ['h','s']
      
      while True:
        
        card_selection = input("Please print your selection: ")
        
        if card_selection in card_option:
          break
        
        else:
          print("That is not a valid option")

    card_choices()

    if card_selection == 's':
      print("This is your final hand {0} it totalls {1}".format(player_hand,sum(math_hand)))
    
      if sum(dealers_hand) > 21:
        print("The dealer has gone bust, you win")
        run_all()
    
      elif sum(dealers_hand) == sum(math_hand):
        print ("The dealer has won as you both got {0}".format(sum(dealers_hand)))
        run_all()
    
      elif sum(dealers_hand) < sum(math_hand):
        print("You have beaten the dealer well done!")
        run_all()
    
      elif sum(math_hand) < sum(dealers_hand):
        print("Unlucky the dealer hast woneth") 
        run_all()

    if card_selection == 'h':
      cars()
      print("This is your hand {0} it totalls {1}".format(player_hand,sum(math_hand)))
      if sum(math_hand) > 21:
        print("You have gone bust, Unlucky better luck next time.")
        run_all()
      else:
        options()
  
  options()


def run_all():
  al_menu()
  all_menu()
  main_game()

run_all()