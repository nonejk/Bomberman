import os
from getchara import *


def clear():
    """ to clear screen
    """
    os.system('clear')


def menu():
    """ display instrucitons and option start or quit game
    """
    clear()
    print("\t\t\t\t\tBOMBERMAN")
    print("\n\n\n\n\n\tInstructions:\t\t\t\t\t\tGame by Sumukh S")
    print("\tw - Up\n\ta - Left\n\ts - Down\n\td - Right\n\tb - Place bomb\n\tq - Quit game")
    print("\n\n\t\t\t\tPress 's' to start the game")
    while(1):
        inp = nonBlockingCharInput()()
        if(inp == "s"):
            break
        if(inp == "q"):
            return -1
