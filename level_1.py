import time

class Level_1: #levels have predefined length, scramble. only need move parsing/validation and main game loop (w win check)

    def __init__(self, commands):
        self.commands = commands
        self.solved = [1,2,3,4,5,6]
        self.current = [1,3,2,5,6,4]
        self.length = len(self.solved)
    
    def level_1(self):
            print("Welcome to level 1. The goal of any level is to permute the given list into a solved state. ")
            time.sleep(1)
            print("A solved state will always look the same: positive numbers from 1 upward. ")
            time.sleep(1)
            print(f"Have a try with {self.current}. Input help if you don't know the move notation. ")
            x = 0
            while True:
                print(f"Current state: {self.current}")
                i, sign = self.get_move()
                self.apply_move(i, sign)
                x+=1
                if self.check():
                    if x > 1:
                        print(f"Congratulations! You solved it in {x} moves!")
                    if x == 1:
                        print(f"Congratulations! You solved it in {x} move!")
                    if not self.level_1_end():
                        break
            return True
        
    def level_1_end(self):
        while True:
            user_input = input("Would you like to try again? Input: ").strip().lower()
            if  user_input == "yes":
                time.sleep(1)
                return True
            elif user_input in self.commands:
                self.commands[user_input]()
            else:
                return False



    def get_move(self):
        while True:
            move = input("Input move: ")
            try:
                i, sign = self.parse_move(move)
            except ValueError as e:
                print(f"Invalid move; {e}")
                continue
            if self.validate_level1(i, sign):
                return i, sign
            else:
                print("Illegal move. ")
        
    def parse_move(self, move):
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

    def validate_level1(self, i, sign):
        if i < 0 or i >= self.length:
            return False
        if sign == "+" and i + 1 >= self.length:
            return False
        if sign == "-" and i - 1 < 0:
            return False
        return True

    def apply_move(self, i, sign):
        if sign == "+":
            self.current[i], self.current[i+1]  = self.current[i+1], self.current[i]
        else:
            self.current[i], self.current[i-1]  = self.current[i-1], self.current[i]

    def check(self):
        if self.current == self.solved:
            return True
