import time #time.sleep()
import sys #sys.exit()
import random #random.choice()

from sandbox import Sandbox

#basic commands (+functions), work globally

def help_func():
    print("help_func!")
    print("test")

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
    "q" : quit_func,
    "exit" : quit_func,
    "leave" : quit_func,
}


def levels(): #for levels ~(TBI)
    print("levels!")


def tosandbox(): #initializes object for sandbox mode and starts it
    while True:
        try:
            length = int(input("Input length: ").strip())
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
