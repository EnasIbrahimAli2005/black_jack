# My project graduation from level 1
import os
import time
import random

def system():
     if os.name=="nt":
       os.system("cls")
     else:
        os.system("clear")
def deal_cards():
    cards=[11,2,3,4,5,6,7,8,9,10,10,10]
    card=random.choice(cards)
    return card
def counting_cards(cards):
   """"تاخد قائمة من الكروت وترجع مجموعهم"""
   #هل يوجد بلاك جاك 
   if sum(cards)==21 and len(cards)==2:
      return 0
   #هل الكروت فوق ال21 وهناك كارت فوق ال11
   if 11 in cards and sum(cards)>21:
      cards.remove(11)
      cards.append(1)
   return sum(cards)   
def compare(user_score,computer_score):
   results={
      "drow":"Drow ☺\n\n",
      "user_over":"You went over 21, Sorry 🙄\n",
      "computer_over":"Computer went over 21, you win 🥳\n",
      "user_21":"You won with a blackjack 🥳\n",
      "computer_21":"Sorry, computer had a blackjack 😨\n",
      "user_win":"You win🥳\n ",
      "user_lose":"You lose 😥\n"
   }

   if user_score==computer_score:
      return results["drow"]
   elif user_score>21:
      return results["user_over"]
   elif computer_score>21:
      return results["computer_over"]
   elif user_score==0:
      return results["user_21"]
   elif computer_score==0:
      return results["computer_21"]
   elif user_score>computer_score:
      return results["user_win"]
   else:
      return results["user_lose"]
def game():
   user_cards=[deal_cards() for _ in range(2)]
   computer_cards=[deal_cards() for _ in range(2)]
   """for _ in range(2):
      user_card.append(distribuation_cards())
      computer_card.append(distribuation_cards())"""
   game_continue=True
   while game_continue:
      user_score=counting_cards(user_cards)
      computer_score=counting_cards(computer_cards)
      print(f"Your cards are {user_cards}, current score is {sum(user_cards)}")
      time.sleep(1)
      print(f"Computer's first card is {computer_cards[0]}")
      time.sleep(2)
      if user_score==0 or computer_score==0 or user_score>21 or computer_score>21:
         game_continue=False
      else:
         another_card=input("Get another card? Y/N ").lower()
         if another_card=='y':
            user_cards.append(deal_cards())
         else:
            game_continue=False
   while computer_score!=0 and computer_score<17:
      computer_cards.append(deal_cards())
      computer_score=counting_cards(computer_cards)
   print(f"Your final hand: {user_cards} with score {user_score}")
   time.sleep(2)
   print(f"Computer's final hand: {computer_cards} with score {computer_score}")
   print(compare(user_score,computer_score))
   time.sleep(5)
   system()


system()
while input("""Choose a game to start............\n1- Froggy \n2- Twanty one \n3- Snake\n---------\n""").lower()=="twanty one":
   print("""
  _______                  _                            
 |__   __|                | |                           
    | |_      ____ _ _ __ | |_ _   _    ___  _ __   ___ 
    | \ \ /\ / / _` | '_ \| __| | | |  / _ \| '_ \ / _ \\
    | |\ V  V / (_| | | | | |_| |_| | | (_) | | | |  __/
    |_| \_/\_/ \__,_|_| |_|\__|\__, |  \___/|_| |_|\___|
                                __/ |                   
                               |___/                        
 """)
   
   print("Starting game............")
   time.sleep(5)
   system()
   game()

   