#RPS.py
#Name:Louis Safranek
#Date:02/05/26
#Assignment:Lab 3
import random

def main():
  wins = 0
  ties = 0
  losses = 0
  playAgain=True
  #Create a loop that continues as long as the user wants to play.
  #User can play as many games as they wish.

  #Randomly choose the computer between 'R', 'P', or 'S'
  #Prompt the user for their RPS selection
  #Determine winner and state what happened to the user
  #Ask the user if they would like to play again.
  while playAgain:
    print("")
    choices=("R","P","S")
    RPS= input("Rock, Paper, or Scisssors? (Please only enter R, P, or S)")
    CRPS= random.choice(choices)
    if (RPS != "R") and (RPS != "P") and (RPS != "S"):
      print("That's not a valid choice!")
    elif (CRPS=="R" and RPS=="S") or (CRPS=="S" and RPS=="P") or (CRPS=="P" and RPS=="R"):
      losses += 1
      print("Computer played " + CRPS)
      print("You lost to a computer. That's just embarassing!")
    elif (CRPS=="R" and RPS=="P") or (CRPS=="P" and RPS=="S") or (CRPS=="S" and RPS=="R"):
      wins += 1
      print ("Computer played " + CRPS)
      print("You won! You were playing a computer though so that's not much of an accomplishment")
    else:
      ties += 1
      print ("Computer played " + CRPS)
      print ("It's a tie! How dare you choose the same answer as me?!?")
    playAgain=input("Would you like to play again? (Y or N)")
    if playAgain=="N":
      playAgain=False
  #In the end, print the stats
  print("Wins \t Ties \t Losses")
  print("---- \t ---- \t ------")
  print(wins, "\t", ties , "\t", losses)

if __name__ == '__main__':
  main()
