import time
from .levelsbase import LevelsBase
class Level_1(LevelsBase):

    def __init__(self,commands):
        super().__init__(commands)
        self.solved = self.solved_3.copy()
        self.scrambled = [1, 3, 2, 5, 6, 4]
        self.current = [1, 3, 2, 5, 6, 4]
        self.length = len(self.solved)
    
    def start(self): #greets user, starts level
            print("Welcome to level 1. The goal of any level is to permute the given centipede into a solved state. ")
            time.sleep(1)
            print("A solved state will always look the same: positive numbers from 1 upward. ")
            time.sleep(1)
            print(f"Have a try with {self.current} - you can almost certainly solve this intuitively. Input help if you don't know the move notation, or if you need help in general. ")
            print("Have fun!")
            if self.play_level():
                return True
            else:
                return False

    def validate(self, i, sign): #validates for adjacent swap move type
        if i < 0 or i >= self.length:
            print("Illegal move; position not in bounds. ")
            return False
        if sign == "+" and i + 1 >= self.length:
            print("Illegal move; right is an impossible direction for given position. ")
            return False
        if sign == "-" and i - 1 < 0:
            print("Illegal move; left is an impossible direction for given position. ")
            return False
        return True

    def permute(self, i, sign): #adjacent swap move type
        if sign == "+":
            self.current[i], self.current[i+1] = self.current[i+1], self.current[i]
        else:
            self.current[i], self.current[i-1] = self.current[i-1], self.current[i]

