"""
sandbox is a separate game mode. it is fundamentally different from the levels mode, insofar as user can choose length and move type freely.
for the sake of simplicity, every aspect of sandbox mode is covered here, from I/O to logic. this is INTENTIONAL.
one thing that could change regarding this is the methods in general. currently theres no clear separation between what interacts with the user, what actually interacts with the list and what just loops it all...
"""

import sys #sys.exit()
import random #random.choice()
import time #time.sleep()

class Sandbox:

    def  __init__(self, commands): #constructor
        self.commands = commands
        self.length = self.get_length()
        self.sandbox_yes = {
        "yes" : self.y,
        "y" : self.y,
        "yeah" : self.y,
        "ye" : self.y,
        "yea" : self.y,
        "okay" :self.y
        }
        self.solved_centipede = list(range(1, self.length + 1))
        self.current_centipede = self.solved_centipede.copy()
        self.scramble()

    def get_length(self): #gets length. once different move types get implemented, this could integrate with options() really well.
        while True:
            length = input("Input length: ").strip().lower()
            if length in self.commands:
                self.commands[length]()
                continue
            try:
                length = int(length)
                if length < 3:
                    print("Length can't be this short!")
                else:
                    return length
            except ValueError:
                print("Not a valid integer!")

    def sandbox(self):
        while True: #main loop
            self.start()
            self.game()
            if self.sandbox_end():
                return True
            else:
                return False
    
    def sandbox_end(self):
        while True:
            user_input = input("Would you like to try again? Input: ").strip().lower()
            if  user_input in self.sandbox_yes:
                self.sandbox_yes[user_input]()
                return True
            elif user_input in self.commands:
                self.commands[user_input]()
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

""" 
#something like this will be used once multiple move types are possible
    def options(self):
        print("You're in sandbox mode. To proceed, input desired length and move type. ")
        print("Available move types: adjacent")
        while True:
            centipede_length = get_length()
            return centipede_length
"""
