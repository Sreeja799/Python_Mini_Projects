from replit import clear

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

print(logo)
dict = {}
choice = 'yes'

while True: 
    n = input('What is you name?: ')
    b = int(input("What's your bid: ")[1:])
    dict[n] = b
    choice = input('Are there any other bidders?: ')
    
    if (choice == 'yes'):
        clear()
        
    else:
        bid = 0
        for i in dict:
            if dict[i] > bid:
                bid = dict[i]
                winner = i
        print(f'The winner is {winner} with a bid of {bid}')
        break