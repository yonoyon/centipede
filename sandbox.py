import sys #sys.exit()
import random #random.choice()
import time #time.sleep()

class Sandbox:

    def  __init__(self, length, commands): #constructor
        self.length = length
        self.commands = commands
        self.sandbox_yes = {
        **commands,
        "yes" : self.y,
        "y" : self.y,
        "yeah" : self.y,
        "ye" : self.y,
        "yea" : self.y,
        "okay" :self.y
        }
        self.solved_centipede = list(range(1, length + 1))
        self.current_centipede = self.solved_centipede.copy()
        self.scramble()

    def sandbox(self):
        while True: #main loop
            self.start()
            self.game()
            print("Would you like to try again?")
            user_input = input("Input here: ").strip().lower()
            if  user_input in self.sandbox_yes: #add in commands case ~ (TBI)
                self.sandbox_yes[user_input]()
                return True
            else:
                return False
    
    def y(self): 
        print("Continuing...")
        time.sleep(1)

    def start(self): #start messages 
        print(f"You must solve into: {self.solved_centipede}")
        print(f"Your scrambled state is: {self.current_centipede}")

    def game(self): #main game loop
        x = 0 #move counter
        while True:
            move = input("Input move: ").strip().lower()
            if move in self.commands:
                self.commands[move]()
                print(f"Current state: {self.current_centipede}")
                continue
            try:
                i, sign = self.parse_move(move)
            except ValueError as e:
                print(f"Invalid Input: {e}")
                continue
            if self.permute(i, sign):
                x+=1
            else:
                print("Invalid move. ")
            if self.check():
                if x > 1:
                    print(f"Congratulations! You solved it in {x} moves!")
                if x == 1:
                    print(f"Congratulations! You solved it in {x} move!")
                break

    def parse_move(self, move): #only for parsing of moves, not for validation
            
        if len(move) < 2:
            raise ValueError("Too short. ")

        try:
            i = int(move[:-1]) - 1
        except ValueError: 
            raise ValueError("Not a valid position. ")
        
        sign = move[-1]
        if sign not in "+-":
            raise ValueError("Not a valid direction. ")
    
        return i, sign

    def generate(self): #generates possible moves
        moves = []
        for i in range(self.length):
            if self.validate(i, "+"):
                moves.append((i, "+"))
            if self.validate(i, "-"):
                moves.append((i, "-"))
        return moves
    
    def scramble(self): #scrambles using generated moves
        for _ in range(self.length*self.length):
            i, sign = random.choice(self.generate())
            self. swap(i, sign)
            #check whether this doesn't scramble it into a solved state already ~ (TBI)

    def permute(self, i, sign): #main puzzle mechanic
        if self.validate(i, sign):
            self.swap(i, sign)
            print(f"Current state: {self.current_centipede}")
            return True
        return False

    def validate(self, i, sign): #validates moves (either generated or input ones)
        if i < 0 or i >= self.length:
            #print("Illegal move; position not in bounds. ") ~ possible error message (TBI)
            return False
        if sign == "+" and i + 1 >= self.length:
            #print("Illegal move; right is an impossible direction for given position. ") ~ possible error message (TBI)
            return False
        if sign == "-" and i - 1 < 0:
            #print("Illegal move; left is an impossible direction for given position. ") ~ possible error message (TBI)
            return False
        return True

    def swap(self, i, sign): #main puzzle logic. used for scrambling and solving. not sure how im gonna implement the multiple move sandbox system yet, ~ (TBI)
        if sign == "+":
            self.current_centipede[i], self.current_centipede[i+1]  = -self.current_centipede[i+1], -self.current_centipede[i]
        else:
            self.current_centipede[i], self.current_centipede[i-1]  = -self.current_centipede[i-1], -self.current_centipede[i]
    
    def check(self): #very simple, "independent" method
        if self.current_centipede == self.solved_centipede:
            return True
