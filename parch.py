from random import randint
import os

# FUNCTIONS
def roll_dices():
    dice1 = randint(1, 6)
    dice2 = randint(1, 6)
    return dice1, dice2

# VARIABLES
player_lives = 3
roll_count = 0
acum_dices = 0
status = True

# MAIN
while status:

    os.system('cls' if os.name == 'nt' else 'clear')

    dices = roll_dices()
    roll_count += 1

    dices_add = dices[0] + dices[1]
    acum_dices += dices_add

    print("#" * 20)
    print(f"Roll dices N°: {roll_count}")
    print("#" * 20)

    print(f"Player lives: {player_lives}")
    print(f"Dice 1: {dices[0]}")
    print(f"Dice 2: {dices[1]}")
    print(f"Dices addition: {dices_add}")

    # WIN GAME
    if acum_dices >= 20:
        print("::: CONGRATULATIONS, YOU'VE WIN :::")
        break

    # LOSE LIFE
    if dices_add % 2 != 0:
        player_lives -= 1
        print(f"You've lost one life. Now you have {player_lives} lives")

        if player_lives == 0:
            print("::: GAME OVER :::")
            break

    # WIN EXTRA LIFE
    if (dices[0] == 6 and dices[1] == 6) or (dices[0] == 1 and dices[1] == 1):
        player_lives += 1
        print("You've won one extra life!")

    input("\nPress ENTER to roll dices again...")