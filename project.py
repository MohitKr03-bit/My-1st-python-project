#Rock Paper Scissors
#Rules:- Rock wins against Scissors, Scissors win against Paper, Paper wins against Rock

Rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_images = [Rock, paper, scissors]

import random
user_choice = int(input("Enter your choice: Type 0 for rock, 1 for paper, 2 for scissors."))

if user_choice >= 3 or user_choice < 0:
    print("Invalid number, You Lose.")

else :
    print(game_images[user_choice])

    computer_choice = random.randint(0,2)

    print("computer choice: ")
    print(game_images[computer_choice])

    if (computer_choice == user_choice):
        print("It's a draw.")

    elif(computer_choice == 0 and user_choice == 2):
        print("You Lose.")

    elif(user_choice == 0 and computer_choice == 2):
        print("You Win.")

    elif (computer_choice > user_choice):  #2>0
        print("You Lose.")

    elif (user_choice > computer_choice):  #2>0
        print("You Win.")