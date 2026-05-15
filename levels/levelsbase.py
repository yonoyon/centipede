#naming is a mess..

import time

class LevelsBase:
    
    def __init__(self, commands):
        self.commands = commands
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

    def play_level(self): #main loop for any level LOGIC
        x = 0
        while True:
            self.print_current_state()
            i, sign = self.get_move()
            self.permute(i, sign)
            x+=1
            if self.check():
                if x > 1:
                    self.print_move_count(x, 1)
                if x == 1:
                    self.print_move_count(x, 0)
                if self.level_end():
                    x = 0
                    self.current = self.scrambled.copy()
                    continue
                else:
                    return False

    def input_level_end(self): #IO
        lorem = input("Would you like to try again? Input: ").strip().lower()
        return lorem

    def level_end(self): #called when user finishes level LOGIC
        while True:
            user_input = self.input_level_end()
            if  user_input in self.input_yes:
                self.input_yes[user_input]()
                return True
            elif user_input in self.commands:
                self.commands[user_input]()
            else:
                return False

    def input_move(self):
        move = input("Input move: ")
        return move
    
    def print_invalid_move(self,e):
        print(f"Invalid move; {e}")
    
    def print_illegal_move(self, error):
        print(self.illegal_moves[error])

    def get_move(self): #gets move from user, calls parse_move and validate (level specific) to filter out bad move notation/illegal moves LOGIC
        while True:
            move = self.input_move()
            if self.check_for_commands(move):
                continue
            try:
                i, sign = self.parse_move(move)
            except ValueError as e:
                self.print_invalid_move(e)
                continue
            
            error = self.validate(i, sign)

            if error == "no_error":
                return i, sign

            if error in self.illegal_moves:
                self.print_illegal_move(error)
                continue

    def parse_move(self, move): #see get_move() LOGIC
        if len(move) < 2:
            raise ValueError("Too short (move must consist of direction and position). ")

        try:
            i = int(move[:-1]) - 1
        except ValueError: 
            raise ValueError("Not a valid position. ")
        
        sign = move[-1]
        if sign not in "+-":
            raise ValueError("Not a valid direction. ")
    
        return i, sign

    def check(self): #LOGIC
        return self.current == self.solved

    def check_for_commands(self, thing): #LOGIC
        if thing in self.commands:
            self.commands[thing]()
            return True
