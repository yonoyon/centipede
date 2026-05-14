import time
from levels.levelsbase import LevelsBase
class Level_2(LevelsBase):

    def __init__(self,commands):
        super().__init__(commands)
        self.solved = self.solved_3.copy()
        self.scrambled = [4,5,1,3,6,2]
        self.current = [4,5,1,3,6,2]
        self.length = len(self.solved)
    
    def level_2(self): #greets user, starts level
            print("Welcome to level 2. In this level, you will learn about the extremes - sliding move type. ")
            time.sleep(1)
            print("As mentioned in level 1, the solved state will remain the same for every level, with the exception of its length. ")
            time.sleep(1)
            print(f"Try to figure out how exactly this move type permutes the centipede, and solve it!")
            print(f"Your centipede: {self.current}")
            if self.play_level():
                return True
            else:
                return False

    def validate(self, i, sign): #validates for extremes - sliding move type
        if i < 0 or i >= self.length:
            print("Illegal move; position not in bounds. ")
            return False
        return True

    def permute(self, i, sign): #extremes - sliding move type
        l = self.length
        if sign == "+":
           self.current.insert(l,self.current.pop(i))
        else:
            self.current.insert(0,self.current.pop(i))
            

