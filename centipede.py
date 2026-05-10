import time #time.sleep()
import sys #sys.exit()

from sandbox import Sandbox
from level_1 import Level_1

"""
basic commands (+functions), work globally
"""
def help_func():
    print("Move notation is simple. You must input a position and a direction. ")
    print("Position is input with a number, and direction is input with an operator. ")
    print("An example: 1,3,2,4 -> 1,2,3,4. In order to do this, you can either input 2+ OR 3-. ")
    print("2+ = swap the 2nd number with the number following it; 3- = swap the 3rd number with the number preceding it. ")
    print("The program will reject invalid move notations. ")

def quit_func():
    print("Exiting...")
    time.sleep(1)
    sys.exit("test")

commands = {
    "help" : help_func,
    "h" : help_func,
    "tutorial" : help_func,
    "tut" : help_func,

    "quit" : quit_func,
    "quti" : quit_func,
    "q" : quit_func,
    "exit" : quit_func,
    "leave" : quit_func,
}


def levels():
    print("Levels available: 1")
    #choice = input("Input number of level to play: ")
    while True:
        level = Level_1(commands)
        if not level.level_1():
            print("went thru")
            break


def tosandbox(): #initializes object for sandbox mode and loops it as long as user wants
    while True:
        centipede = Sandbox(commands)
        if centipede.sandbox():
            pass
        else:
            break

"""
main menu stuff below
"""
menu_commands = {
    **commands,

    "levels" : levels,
    "level" : levels,
    "l" : levels,

    "sandbox" : tosandbox,
    "sand" : tosandbox,
    "s" : tosandbox
}

def menu(): #main menu
    print("Welcome! Choose whether you want to play through the levels or enter sandbox mode. ")
    print("Of course, you can also input help at any time, if needed. If you'd like to quit, input quit. ")
    
    while True:
        print("You're in the main menu. ")
        user_input = input("Input here: ").strip().lower()
        if user_input in menu_commands:
            menu_commands[user_input]()
        else:
            print("Input invalid, try again. ")

menu() #start main menu
