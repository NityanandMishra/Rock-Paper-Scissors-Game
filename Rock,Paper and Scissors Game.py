print("Welcome to the Rock,Paper and Scissors game!")
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
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
import random
game_images=[rock,paper,scissors]

user_choice= int(input("What do you choose? Enter 0 for Rock, 1 for Paper and 2 for Scissors\n"))
if user_choice>=3 or user_choice<0:
    print("You have entered an Invalid Input. You lost the game. Better luck next time.")
else:
    print(f"User Chose:{game_images[user_choice]}")
    
    computer_choice = random.randint(0,2)
    print(f"Computer Choice:{game_images[computer_choice]}")
    if user_choice==0 and computer_choice==2:
        print("You lost the game. Better luck next time.")
    elif user_choice==2 and computer_choice==0:
        print("You Won the game. Congratulations!")
    elif user_choice==computer_choice:
        print("Its a draw")
    elif user_choice>computer_choice:
        print("You Won the game. Congratulations!")
    elif user_choice<computer_choice:
         print("You lost the game. Better luck next time.")