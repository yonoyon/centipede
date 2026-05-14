import time
from .levelsbase import LevelsBase
class Level_3(LevelsBase):

    def __init__(self,commands,available_levels):
        super().__init__(commands)
        self.available_levels  = available_levels
        self.solved = self.solved_6.copy()
        self.scrambled = [-4, 6, 1, -3, -2, -5]
        self.current = self.scrambled.copy()
        self.length = len(self.solved)
    
    def start(self): #greets user, starts level
            print("Welcome to level 3. An introduction to the adjacent swap - sign flip move type. ")
            time.sleep(1)
            print("It's easier than it may look like.")
            time.sleep(1)
            print(f"Here's your centipede for this level: {self.current}")
            print(f"Good luck!")
            self.play_level()
            if 4 not in self.available_levels:
                self.available_levels.append(4)
                return False
            return False

    def validate(self, i, sign): #validates for adjacent swap - sign flip move type
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

    def permute(self, i, sign): #adjacent swap - sign flip move type
        if sign == "+":
            self.current[i], self.current[i+1] = -self.current[i+1], -self.current[i]
        else:
            self.current[i], self.current[i-1] = -self.current[i-1], -self.current[i]