import random
logo = '''
   _____                       _   _                                  _               
  / ____|                     | | | |                                | |              
 | |  __ _   _  ___  ___ ___  | |_| |__   ___   _ __  _   _ _ __ ___ | |__   ___ _ __ 
 | | |_ | | | |/ _ \/ __/ __| | __| '_ \ / _ \ | '_ \| | | | '_ ` _ \| '_ \ / _ \ '__|
 | |__| | |_| |  __/\__ \__ \ | |_| | | |  __/ | | | | |_| | | | | | | |_) |  __/ |   
  \_____|\__,_|\___||___/___/  \__|_| |_|\___| |_| |_|\__,_|_| |_| |_|_.__/ \___|_|   
                                                                                      
                                                                                            
'''

print(logo)
num = random.randint(1, 100)
print("Welcome to the number guessing game!\nI'm thinking of a number between 1 to 100")
type = input("Choose a difficulty type: 'easy' or 'hard': ")

print(num)
if type == 'easy':
    guess_count = 10
else:
    guess_count = 5
    
while guess_count != 0:
    guess = int(input("Make a guess: "))
    if (guess == num):
        print("You guessed right! It's", num)
        break
    elif (guess < num):
        print("Too low")
    else:
        print("Too high")

    guess_count -= 1
    print(f"You are left with {guess_count} guesses")

if (guess_count == 0):
    print("You are out of guesses!")