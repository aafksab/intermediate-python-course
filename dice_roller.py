import random
import argparse

parser = argparse.ArgumentParser(description='Args for Dice Rolling')
parser.add_argument('--rolls', dest='dice_rolls', type=int, help='Number of dice to roll')
parser.add_argument('--size', dest='dice_size', type=int, help='Size of dice to roll')
args = parser.parse_args()

dice_rolls = args.dice_rolls
dice_size = args.dice_size

def main(dice_rolls,dice_size):
  dice_sum = 0
  for i in range(0,dice_rolls):
    roll = random.randint(1,dice_size)
    dice_sum += roll
    if roll == 1:
      print(f'You rolled a {roll}! Critical Fail')
    elif roll == dice_size:
      print(f'You rolled a {roll}! Critical Success!')
    else:
      print(f'You rolled a {roll}')
    
  print(f'You have rolled a total of {dice_sum}')
if __name__== "__main__":
  main(dice_rolls,dice_size)