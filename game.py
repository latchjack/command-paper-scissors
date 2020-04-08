import random

# Game variables
items = ['rock', 'paper', 'scissors']

# Player's choice
playerChoice = input('rock, paper, scissors?\n')
print('You choose', playerChoice)

# Computer's choice
computerChoice = random.choice(items)
print('The computer chooses', computerChoice, '\n')

# Game functions
if playerChoice == computerChoice:
  print('\x1b[1;37m' 'It\'s a draw!\n' '\x1b[0;37m')
elif playerChoice == 'rock' and computerChoice == 'scissors' or playerChoice == 'paper' and computerChoice == 'rock' or playerChoice == 'scissors' and computerChoice == 'paper':
  print('\x1b[1;32m' 'You win\n' '\x1b[0;32m')
else:
  print('\x1b[1;31m' 'You lost\n' '\x1b[0;31m')