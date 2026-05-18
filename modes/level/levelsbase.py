#naming is a mess..

import time

class LevelsBase:
    
    def __init__(self):#, commands):
       # self.commands = commands
        self.input_yes = {
        "yes" : self.y,
        "y" : self.y,
        "yeah" : self.y,
        "ye" : self.y,
        "yea" : self.y,
        "okay" : self.y,
        "continue" : self.y
        }
        self.illegal_moves = {
        "oob_error" : "Illegal move; position not in bounds. ",
        "right_impossible_error" : "Illegal move; right is an impossible direction for given position. ",
        "left_impossible_error" : "Illegal move; left is an impossible direction for given position. "
        }
        self.solved = []
        self.scrambled = []
        self.current = []
        self.length = len(self.solved)
        #solved states for levels below (number indicates length)
        self.solved_6 = list(range(1, 7))
        self.solved_8 = list(range(1, 9))
        self.solved_10 = list(range(1, 11))

    def y(self): #a bit unnecessary but whatevs IO
        print("Continuing...")
        time.sleep(1)

    def print_current_state(self):
        print(f"Current state: {self.current}")

    def print_move_count(self, x, count): #IO
        if count == 1:
            print(f"Congratulations! You solved it in {x} moves!")
        else:
            print(f"Congratulations! You solved it in {x} move!")
            
    def input_level_end(self): #IO
        lorem = input("Would you like to try again? Input: ").strip().lower()
        return lorem

    def get_move(self):
        move = input("Input move: ")
        return move
    
    def print_invalid_move(self,e):
        print(f"Invalid move; {e}")
    
    def print_illegal_move(self, error):
        print(self.illegal_moves[error])

    def finish(self):
        return False