import time
from levelsbase import Levelsbase
class Level_1(Levelsbase):

    def __init__(self,commands):
        super().__init__(commands)
        self.solved = [1,2,3,4,5,6]
        self.scrambled = [1,3,2,5,6,4]
        self.current = [1,3,2,5,6,4]
        self.length = len(self.solved)
    
    def level_1(self): #greets user, starts level
            print("Welcome to level 1. The goal of any level is to permute the given list into a solved state. ")
            time.sleep(1)
            print("A solved state will always look the same: positive numbers from 1 upward. ")
            time.sleep(1)
            print(f"Have a try with {self.current} - you can almost certainly solve this intuitively. Input help if you don't know the move notation, or if you need help in general. ")
            print("Have fun!")
            if self.play_level():
                return True
            else:
                return False

    def validate(self, i, sign): #specific to this level (move type)
        if i < 0 or i >= self.length:
            return False
        if sign == "+" and i + 1 >= self.length:
            return False
        if sign == "-" and i - 1 < 0:
            return False
        return True

    def permute(self, i, sign): #specific to this level. probably gonna call this "adjacent swap"
        if sign == "+":
            self.current[i], self.current[i+1]  = self.current[i+1], self.current[i]
        else:
            self.current[i], self.current[i-1]  = self.current[i-1], self.current[i]

