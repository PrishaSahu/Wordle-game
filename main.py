import random
import sys
from termcolor import colored

def print_menu():
  print("Let's play Wordle:")
  print("Type a 5 letter word below and press enter.")

def read_random_word():
  with open("wordle_words.txt") as f:
    words = f.read().splitlines()
    return random.choice(words)
  
print_menu()
word = read_random_word()

for attempt in range(1,7):
  guess = input().lower()
  
  sys.stdout.write('\x1b[1A')
  sys.stdout.write('\x1b[2K')
  
  for i in range(min(len(guess), 5)):
    if guess[i] == word[i]:
      #end= signifies that it will not go to a new       line after input
      print(colored(guess[i], 'green'), end="")
    elif guess[i] in word:
      print(colored(guess[i], 'yellow'), end="")
    else:
      print(guess[i], end="")

  if guess == word:
    print(colored(f"Congrats! You got the wordle in {attempt}", 'light_blue'))
    break

