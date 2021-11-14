import random
import time
import math
from random import randint
from random import *
import os



print(
    """Welcome to the reverse guessing game."""

"""\n----------------------------"""


"""\nIn this game, you must choose a number between 1-10 while the computer has to guess what number you're thinking of."""

"""\n----------------------------"""

"""BEGIN!"""


"""----------------------------"""
)

user_wins = 0
computer_wins = 0


while True: #creates an endless loop 
    



    number1 = (randint(1,10))



    answer = number1


    print()

    max1 = int(input("Please Choose a number between 1-10. ")) # the number must be between the number given at `number1`. The default is 10-30.



    if max1 > 10:
        repeat = input("That is not a valid choice. Please try again: ").lower()

    if max1 < 1:
        repeat = input("That is not a valid choice. Please try again: ").lower()
    



    print("----------------------------")


    if answer == max1:
        print(f"""You lost the game!
        \nYou chose {max1} and I chose {answer} """)

        computer_wins+=1
        print("I have "+str(computer_wins)+" win(s)")

        print("\n----------------------------\n")


    else:
        print(f"""You won! 
        \nI chose {answer} and you chose {max1}""")

        user_wins+=1
        print("You have "+str(user_wins)+" win(s)")
        print("\n----------------------------\n")



    repeat = input("Play again? (Y/N) ").lower()
    while repeat not in ['y', 'n']:
        repeat = input("That is not a valid choice. Please try again: ").lower()
    
    if repeat == 'n':
        break



def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

clearConsole()