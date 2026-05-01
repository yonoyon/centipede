import sys #sys.exit()
import random #random.choice()

solved_centipede = [+1, +2, +3, +4, +5, +6, +7, +8, +9, +10, +11, +12] #define to-be state
n = len(solved_centipede) #length of centipede, necessary for generation of valid moves (for scrambling), and validation of input moves

def parse_move(move): #parses user input, extracts position (i) and direction (sign). outputs corresponding error message if it fails
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

def validate_move(i, sign, n, silent =False): #checks whether move is legal, for both generated and input ones. outputs corresponding error message if it fails (only with user input)
    if i < 0 or i >= n:
        if not silent:
            print("Illegal move; position not in bounds. ")
        return False

    if sign == "+" and i + 1 >= n:
        if not silent:
            print("Illegal move; right is an impossible direction for given position. ")
        return False

    if sign == "-" and i - 1 < 0:
        if not silent:
            print("Illegal move; left is an impossible direction for given position. ")
        return False
    return True

def generate_moves(n): #generates valid moves for scrambling, using validation function
    moves = []
    for i in range(n):
        if validate_move(i, "+", n, silent =True):
            moves.append((i, "+"))
        if validate_move(i, "-", n, silent=True):
            moves.append((i, "-"))
    return moves

def scramble(solved_centipede, n): #scrambles centipede using generated moves
   centipede = solved_centipede.copy()
   for _ in range(n*n):
        moves = generate_moves(n)
        i, sign = random.choice(moves)
        if sign == "+":
             swap_positive(centipede, i)
        else:
             swap_negative(centipede, i)
        
   return centipede

def swap_positive(centipede, i): #swapping function, positive (right) direction
    centipede[i], centipede[i+1]  = -centipede[i+1], -centipede[i]

def swap_negative(centipede, i): #swapping function, negative (left) direction
    centipede[i], centipede[i-1]  = -centipede[i-1], -centipede[i]

scrambled_centipede = scramble(solved_centipede, n) #define scrambled and current centipede
current_centipede = scrambled_centipede.copy()

print(f"You must solve into: {solved_centipede}") #display goal and scrambled centipede
print(f"Your scrambled state is: {scrambled_centipede}")

while True: #main loop
    print(f"Current state: {current_centipede}")
    move = input("Input move: ")
    try:
        i, sign = parse_move(move)
    except ValueError as e:
        print(f"Invalid Input: {e}")
        continue
    if validate_move(i, sign, n):
        if sign == "+":
            swap_positive(current_centipede, i)
        else:
            swap_negative(current_centipede, i)
        if current_centipede == solved_centipede:
            print(f"Congratulations! You solved it: {current_centipede}")
            break
    else:
        continue
