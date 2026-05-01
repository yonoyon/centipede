import sys #sys.exit()

def parse_move(move): #parses user input, extracts position (i) and direction (sign). outputs corresponding error message if it fails.
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

def check_move(i, sign, n): #checks whether move is legal. outputs corresponding error message if it fails.
    if i < 0 or i >= n:
        print("Illegal move; position not in bounds. ")
        return False

    if sign == "+" and i + 1 >= n:
        print("Illegal move; right is an impossible direction for given position. ")
        return False

    if sign == "-" and i - 1 < 0:
        print("Illegal move; left is an impossible direction for given position. ")
        return False
    return True
        


def swap_positive(centipede, i): #swapping function, positive (right) direction
    centipede[i], centipede[i+1]  = -centipede[i+1], -centipede[i]

def swap_negative(centipede, i): #swapping function, negative (left) direction
    centipede[i], centipede[i-1]  = -centipede[i-1], -centipede[i]


centipede = [-1, +2, +3, +4, +5] #define values, print at start
n = len(centipede)
print(centipede)

while True: #main loop
    move = input("Input move: ")
    try:
        i, sign = parse_move(move)
    except ValueError as e:
        print(f"Invalid Input: {e}")
        continue
    if check_move(i, sign, n):
        if sign == "+":
            swap_positive(centipede, i)
        else:
            swap_negative(centipede, i)
        print(centipede)
    else:
        continue