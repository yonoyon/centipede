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
    sys.exit()

def q(): #exits program
    print("Exiting...")
    time.sleep(1)
    sys.exit()

ynqe = { #see functions above
    "yes" : y,
    "y" : y,
    "yeah" : y,
    "ye" : y,
    "yea" : y,
    "no" : n,
    "nah" : n,
    "naw" : n,
    "na" : n,
    "n" : n,
    "quit" : q,
    "q" : q,
    "exit" : q,
    "leave" : q
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

def game(): #game function/loop
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
            user_input = input("Would you like to try again? (y/n)").strip().lower()
            if user_input in ynqe: #for actions (see ynqe dictionary)
                ynqe[user_input]()
                break
            else:
                q()

while True: #main loop
    try:
        length = int(input("Input length: ").strip())
        if length < 3:
            print("Length can't be this short!")
            continue
        centipede_1 = Centipede(length)
        centipede_1.start()
        game()
    except ValueError:
        print("Not a valid integer!")

