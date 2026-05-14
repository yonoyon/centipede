import time
from levels.levelsbase import LevelsBase
class Level_3(LevelsBase):

    def __init__(self,commands):
        super().__init__(commands)
        self.solved = self.solved_3.copy()
        self.scrambled = [-4, 6, 1, -3, -2, -5]
        self.current = [-4, 6, 1, -3, -2, -5]
        self.length = len(self.solved)
    
    def level_3(self): #greets user, starts level
            print("Welcome to level 3. You will be introduced to the adjacent swap - sign flip move type. ")
            time.sleep(1)
            print("It's easier than it may look like.")
            time.sleep(1)
            print(f"Here's your centipede for this level: {self.current}")
            print(f"Good luck!")
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
            self.current[i], self.current[i+1] = -self.current[i+1], -self.current[i]
        else:
            self.current[i], self.current[i-1] = -self.current[i-1], -self.current[i]