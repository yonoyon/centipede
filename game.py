import time #sleep()
import sys #exit()
import random #choice()

from centipede import Centipede

def y(): #continues if user wants to
    print("Continuing...")
    time.sleep(1)
def n(): #exits program
    print("Exiting...")
    time.sleep(1)
def q(): #exits program
    print("Exiting...")
    time.sleep(1)

yes = { #see functions above
    "yes" : y,
    "y" : y,
    "yeah" : y,
    "ye" : y,
    "yea" : y
    }

def parse_move(move): #parses move, extracting position and direction
    move = move.strip().lower()
    
    if move == "quit": #use dictionary for better logic ~ (TBI)
        q()
    
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
           





def levels():
    print("levels!")

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
            user_input = input("Would you like to try again?").strip().lower()
            if  user_input in yes:
                yes[user_input]()
            else:
                break
        except ValueError:
            print("Not a valid integer!")


def help_func():
    print("help_func!")
    
def quit_func():
    print("quit_func!")
    sys.exit()



menu_options = {
    "levels" : levels,
    "level" : levels,
    "l" : levels,

    "sandbox" : sandbox,
    "sand" : sandbox,
    "s" : sandbox,

    "help" : help_func,
    "h" : help_func,
    "tutorial" : help_func,
    "tut" : help_func,

    "quit" : quit_func,
    "q" : quit_func,
    "exit" : quit_func,
    
    "1" : levels,
    "2" : sandbox,
    "3" : help_func,
    "4": quit_func
}

def menu():
    print("Welcome! Choose whether you want to play through the levels or enter sandbox mode. ")
    print("Of course, you can also input help at any time, if needed. If you'd like to quit, input quit. ")
    
    
    while True:
        print("Main menu")
        user_input = input("Input here: ").strip().lower()
        if user_input in menu_options:
            menu_options[user_input]()
            print("menu?")
        else:
            print("Input invalid, try again. ")
    print("passed loop!")







menu()


"""
#you can uncomment this if you want some more "fun"
def funny(): 
    while True:
        try:
            print(random.choice(["lorem ipsum", "lorem ipsum", "lorem ipsum"]))
            time.sleep(0.3)
        except KeyboardInterrupt:
            while True:
                try:
                    print("lorem ipsum")
                except KeyboardInterrupt:
                    while True:
                        try:
                            print("lorem ipsum")
                        except KeyboardInterrupt:
                            while True:
                                try:
                                    print("lorem ipsum")
                                except KeyboardInterrupt:
                                    print("lorem ipsum")
                                    q()
#make sure to add this to the dictionary
    "lorem ipsum" : funny,
    "lorem ipsum" : funny,
    "lorem ipsum" : funny
#of course, this will only work if you insert it correctly. have fun!
""" 
