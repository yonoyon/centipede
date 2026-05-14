import time #time.sleep()
import sys #sys.exit()

from sandbox.sandbox import SandBox
from levels import Level_1, Level_2, Level_3, Level_4, Level_5, Level_6

"""
basic commands (+functions), work globally. could look into separation of sandbox and levels mode even more by splitting these as well.. not sure yet.
"""
def help_func():
    print("The program will reject invalid move notation. Every input field is designed to accept quit and help as possible commands. ")
    print("Move notation is simple. You must input a position and a direction. ")
    print("Position is input with a number, direction with an operator. ")
    print("An example permutation: [1,3,2,4] to [1,2,3,4]. You can input either 2+ or 3- for this. ")
    print("2+ swaps the 2nd number with the number following it; 3- swaps the 3rd number with the number preceding it - so in the end, it does the same.")
    print("This, of course, only applies to this specific move type. Move notation will remain the same, whereas move type will not.")
    print("Play through the levels to find out what move types exist!")
    

def quit_func():
    print("Exiting...")
    time.sleep(1)
    sys.exit("Successfully quit centipede. ")

commands = {
    "help" : help_func,
    "hepl" : help_func,
    "h" : help_func,
    "hrlp" : help_func,
    "tutorial" : help_func,
    "tut" : help_func,

    "quit" : quit_func,
    "quti" : quit_func,
    "q" : quit_func,
    "exit" : quit_func,
    "leave" : quit_func,
}

"""
dicts for levels, levels func itself
"""

input_back = {
    "back" : 0,
    "return" : 0,
    "go back" : 0
}


level_names = {
    1 : Level_1,
    2 : Level_2,
    3 : Level_3,
    4 : Level_4,
    5 : Level_5,
    6 : Level_6
}

def levels(): #loop for level mode. pre-level input validation could be moved into LevelsBase ~ (TBI)
    available_levels = list(level_names.keys())
    print(f"Currently available levels: {available_levels} ")
    
    while True:
        choice = input("Input level to play: ").strip().lower()
        if choice in commands:
            commands[choice]()
            continue
        if choice in input_back:
            break

        try:
            choice = int(choice)
        except ValueError:
            print("Input a number. ")
            continue

        if choice not in available_levels:
            print("Level unavailable. ")
            continue
        
        if choice in level_names:
            level = level_names[choice](commands)
            if not level.start():
                break

def tosandbox(): #initializes object for sandbox mode and loops it as long as user wants
    while True:
        centipede = SandBox(commands)
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
    "s" : tosandbox,
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
