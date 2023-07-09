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

#Write your code below this line 👇
import random
choice = int(input('What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors.\n'))

if (choice == 0):
  print(rock)
elif (choice == 1):
  print(paper)
else:
  print(scissors)
  
comp = random.randint(0, 2)
if (comp == 0):
  print(rock)
elif (comp == 1):
  print(paper)
else:
  print(scissors)

if (choice == comp):
  print('Tie')
elif (choice == 0 and comp == 1) or (choice == 1 and comp == 2) or (choice == 2 and comp == 0):
  print('You lose.')
elif (choice == 0 and comp == 2) or (choice == 1 and comp == 0) or (choice == 2 and comp == 1):
  print('You won.')
