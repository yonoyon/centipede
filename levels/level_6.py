import time
from .levelsbase import LevelsBase
class Level_6(LevelsBase):

    def __init__(self,commands):
        super().__init__(commands)
        self.solved = self.solved_10.copy()
        self.scrambled = [5, -8, -1, -6, -3, 10, -9, -2, -7, -4]
        self.current = self.scrambled.copy()
        self.length = len(self.solved)
    
    def start(self): #greets user, starts level
            print("Welcome to level 6. This is the last level before your first challenge. ")
            time.sleep(1)
            print("You probably already saw this coming. The jump swap - sign flip move type.")
            time.sleep(1)
            print(f"And here's a fun fact: if a segment can never reach a specific position, then a permutation with the segment in that position as a target is impossible to achieve. ")
            print(f"Enough said, you know the drill: {self.current}")
            if self.play_level():
                return True
            else:
                return False

    def validate(self, i, sign): #validates for jump swap - sign flip move type
        if i < 0 or i >= self.length:
            print("Illegal move; position not in bounds. ")
            return False
        if sign == "+" and i + 2 >= self.length:
            print("Illegal move; right is an impossible direction for given position. ")
            return False
        if sign == "-" and i - 2 < 0:
            print("Illegal move; left is an impossible direction for given position. ")
            return False
        return True

    def permute(self, i, sign): #adjacent jump swap -sign flip move type
        if sign == "+":
            self.current[i], self.current[i+2] = -self.current[i+2], -self.current[i]
        else:
            self.current[i], self.current[i-2] = -self.current[i-2], -self.current[i]