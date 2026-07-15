import sys

print("")
player_choice = input("Enter ...\n1 for Rock \n2 for Paper \n3 for Scissors \n")
print(player_choice)

player = int(player_choice) 

if player < 1 or player > 3:
    sys.exit("You must enter 1, 2, or 3.")