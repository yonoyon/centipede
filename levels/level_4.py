import time
from .levelsbase import LevelsBase
class Level_4(LevelsBase):

    def __init__(self,commands):
        super().__init__(commands)
        self.solved = self.solved_10.copy()
        self.scrambled = [5,10,7,2,9,6,1,4,3,8]
        self.current = self.scrambled.copy()
        self.length = len(self.solved)
    
    def start(self): #greets user, starts level
            print("Welcome to level 4. This one is going to introduce the jump swap move type. ")
            time.sleep(1)
            print("It, essentially, is a copy of the adjacent swap, except that you jump over one segment and swap with the next one. ")
            time.sleep(1)
            print(f"For this move type, you're getting a longer centipede: {self.current}")
            print(f"Good luck!")
            if self.play_level():
                return True
            else:
                return False

    def validate(self, i, sign): #validates for jump swap move type
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

    def permute(self, i, sign): #adjacent jump swap move type
        if sign == "+":
            self.current[i], self.current[i+2] = self.current[i+2], self.current[i]
        else:
            self.current[i], self.current[i-2] = self.current[i-2], self.current[i]