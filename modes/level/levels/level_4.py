import time
from .levelsbase import LevelsBase
from .levelslogic import LevelsLogic

class Level_4(LevelsBase, LevelsLogic):

    def __init__(self,commands,available_levels):
        super().__init__(commands)
        self.available_levels  = available_levels
        self.solved = self.solved_10.copy()
        self.scrambled = [5, 10, 7, 2, 9, 6, 1, 4, 3, 8]
        self.current = self.scrambled.copy()
        self.length = len(self.solved)
    
    def start(self):
        self.play_level()
        if 5 not in self.available_levels:
            self.available_levels.append(5)
        return False
    
    def welcome(self):
        print("Welcome to level 4. This one is going to introduce the jump swap move type. ")
        time.sleep(1)
        print("It, essentially, is a copy of the adjacent swap, except that you jump over one segment and swap with the next one. ")
        time.sleep(1)
        print(f"For this move type, you're getting a longer centipede: {self.current}")
        print(f"Good luck!")

    def validate(self, i, sign): #validates for jump swap move type
        if i < 0 or i >= self.length:
            return "oob_error"
        if sign == "+" and i + 2 >= self.length:
            return "right_impossible_error"
        if sign == "-" and i - 2 < 0:
            return "left_impossible_error"
        return "no_error"

    def permute(self, i, sign): #adjacent jump swap move type
        if sign == "+":
            self.current[i], self.current[i+2] = self.current[i+2], self.current[i]
        else:
            self.current[i], self.current[i-2] = self.current[i-2], self.current[i]