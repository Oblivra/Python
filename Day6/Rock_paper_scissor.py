# Rules:
'''
Rock crushes Scissors
Scissors cuts Paper
Paper covers Rock
'''

import random
computer = random.choice([-1,0,1])                              #number
user = input("Enter your choice (Rock, Paper, Scissors): ")     #text

options = {'rock': -1, 'paper': 0, 'scissors': 1}
value = {-1: 'rock', 0: 'paper', 1: 'scissors'}

user_value = user.lower()                                      #text
computer_value = value[computer]                               #text


print("--------------------------------")
print(f" computer choosed : {computer_value}\n You choosed      : {user_value}")
print("--------------------------------")
if user_value not in options:
    print("")
    print("🙄-------Invalid choice!-------🙄")
    print("")
else:
    User = options[user_value]                                  #number

    if User == computer:
        print("")
        print("😏😏😏😏😏😏😏😏 It's a tie! 😏😏😏😏😏😏😏😏")
        print("")
    elif (User == -1 and computer == 1) or (User == 1 and computer == 0) or (User == 0 and computer == -1):
        print("")
        print("😎😎😎😎😎😎😎😎 You win! 😎😎😎😎😎😎😎😎")
        print("")
    else:
        print("")
        print("😢😢😢😢😢😢😢😢 You lose! 😢😢😢😢😢😢😢😢")
        print("")
