import time
from .levelsbase import LevelsBase
class Level_2(LevelsBase):

    def __init__(self,commands,available_levels):
        super().__init__(commands)
        self.available_levels  = available_levels
        self.solved = self.solved_6.copy()
        self.scrambled = [4, 5, 1, 3, 6, 2]
        self.current = self.scrambled.copy()
        self.length = len(self.solved)
    
    def start(self):
        self.play_level()
        if 3 not in self.available_levels:
            self.available_levels.append(3)
        return False

    def welcome(self):
        print("Welcome to level 2. In this level, you will learn about the extremes move type. ")
        time.sleep(1)
        print("As mentioned in level 1, the solved state will remain the same for every level, with the exception of its length. ")
        time.sleep(1)
        print(f"Try to figure out how exactly this move type permutes the centipede, and solve it!")
        print(f"Your centipede: {self.current}")

    def validate(self, i, sign): #validates for extremes move type
        if i < 0 or i >= self.length:
            return "oob_error"
        return "no_error"

    def permute(self, i, sign): #extremes move type
        l = self.length
        if sign == "+":
           self.current.insert(l,self.current.pop(i))
        else:
            self.current.insert(0,self.current.pop(i))
            

