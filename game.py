import time #sleep()
import sys #exit()
import random #choice()

from centipede import Centipede

#main commands, work globally

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


def parse_move(move): #parses move, extracting position and direction
    move = move.strip().lower()
    
    if move in commands:
        move[commands]()
    
    if len(move) < 2:
        raise ValueError("Too short. ")

    try:
        i = int(move[:-1]) - 1
    except ValueError: 
        raise ValueError("Not a valid index. ")
        
    sign = move[-1]
    if sign not in "+-":
        raise ValueError("Not a valid operator. ")
    
    return i, sign

def game(centipede_1): #game function/loop
    x = 0 #move counter
    while True:
        move = input("Input move: ")
        try:
            i, sign = parse_move(move)
        except ValueError as e:
            print(f"Invalid Input: {e}")
            continue
        if centipede_1.permute(i, sign):
            x+=1
        else:
            print("Invalid move. ")
        if centipede_1.check(x):
           break

def levels(): #for levels
    print("levels!")


"""
dictionary+function, main function for sandbox mode
"""
def y(): 
    print("Continuing...")
    time.sleep(1)

sandbox_yes = {
    **commands,
    "yes" : y,
    "y" : y,
    "yeah" : y,
    "ye" : y,
    "yea" : y,
    "okay" :y,
    }

def sandbox():
    print("sandbox!")
    while True: #main loop
        try:
            length = int(input("Input length: ").strip())
            if length < 3:
                print("Length can't be this short!")
                continue
            centipede_1 = Centipede(length)
            centipede_1.start()
            game(centipede_1)
            print("Would you like to try again?")
            user_input = input("Input here: ").strip().lower()
            if  user_input in sandbox_yes:
                sandbox_yes[user_input]()
            else:
                break
        except ValueError:
            print("Not a valid integer!")
            
"""
main menu stuff
"""

menu_commands = {
    **commands,

    "levels" : levels,
    "level" : levels,
    "l" : levels,

    "sandbox" : sandbox,
    "sand" : sandbox,
    "s" : sandbox

}

def menu():
    print("Welcome! Choose whether you want to play through the levels or enter sandbox mode. ")
    print("Of course, you can also input help at any time, if needed. If you'd like to quit, input quit. ")
    
    while True:
        print("You're in the main menu. ")
        user_input = input("Input here: ").strip().lower()
        if user_input in menu_commands:
            menu_commands[user_input]()
        else:
            print("Input invalid, try again. ")
    print("passed loop!")

menu()#starts
