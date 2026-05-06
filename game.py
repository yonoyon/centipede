import sys #sys.exit()

from centipede import Centipede

while True: #gets length from user input
    try:
        length = int(input("Input length: ").strip())
        if length < 3:
            print("Length can't be this short!")
            continue
        break
    except ValueError:
        print("Not a valid integer!")

centipede_1 = Centipede(length) #first (and only) object lol

def parse_move(move): #parses move, extracting position and direction
    move = move.strip().lower()
    
    if move == "quit":
        sys.exit()
    
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

centipede_1.start() #start message

x = 0 #define counter

while True: #main loop
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
    centipede_1.check(x)
