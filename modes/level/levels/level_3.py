import time
from ..levelsmode import LevelsMode

class Level_3(LevelsMode):
    def __init__(self,commands,available_levels):
        super().__init__(commands)
        self.available_levels  = available_levels
        self.solved = self.solved_6.copy()
        self.scrambled = [-4, 6, 1, -3, -2, -5]
        self.current = self.scrambled.copy()
        self.length = len(self.solved)
    
    def start(self):
        self.play_level()
        if 4 not in self.available_levels:
            self.available_levels.append(4)
        return False
    
    def welcome(self):
        print("Welcome to level 3. An introduction to the adjacent swap - sign flip move type. ")
        time.sleep(1)
        print("It's easier than it may look like.")
        time.sleep(1)
        print(f"Here's your centipede for this level: {self.current}")
        print(f"Good luck!")

    def validate(self, i, sign): #validates for adjacent swap - sign flip move type
        if i < 0 or i >= self.length:
            return "oob_error"
        if sign == "+" and i + 1 >= self.length:
            return "right_impossible_error"
        if sign == "-" and i - 1 < 0:
            return "left_impossible_error"
        return "no_error"

    def permute(self, i, sign): #adjacent swap - sign flip move type
        if sign == "+":
            self.current[i], self.current[i+1] = -self.current[i+1], -self.current[i]
        else:
            self.current[i], self.current[i-1] = -self.current[i-1], -self.current[i]