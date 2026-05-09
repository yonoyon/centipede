#levels mode TBI!!!

import time #time.sleep()
import sys #sys.exit()

from sandbox import Sandbox
#from level_1 import Level_1 ~ (TBI)

#basic commands (+functions), work globally

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


def levels(): #for levels ~(TBI)
    print("levels")
    
    #while True:
     #   level_1 = Level_1(commands)
      #  if level_1.level_1():
       #     break
    


def tosandbox(): #initializes object for sandbox mode and starts it
    while True:
        length = input("Input length: ").strip().lower()
        if length in commands:
            commands[length]()
            continue
        try:
            length = int(length)
            if length < 3:
                print("Length can't be this short!")
            else:
                centipede_1 = Sandbox(length, commands)
                if centipede_1.sandbox():
                    pass
                else:
                    break
        except ValueError:
            print("Not a valid integer!")
        

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
