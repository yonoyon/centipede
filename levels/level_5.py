import time
from .levelsbase import LevelsBase
class Level_5(LevelsBase):

    def __init__(self,commands,available_levels):
        super().__init__(commands)
        self.available_levels  = available_levels
        self.solved = self.solved_8.copy()
        self.scrambled = [-2, 5, 7, 1, -3, 8, -4, -6]
        self.current = self.scrambled.copy()
        self.length = len(self.solved)
    
    def start(self):
        self.play_level()
        if 6 not in self.available_levels:
            self.available_levels.append(6)
        return False

    def welcome(self):
        print("Welcome to level 5. Don't worry, nothing too new - this level will teach you a variation of the extremes move type, one with sign flips... ")
        time.sleep(1)
        print("So, the extremes - sign flip move type. ")
        time.sleep(1)
        print(f"Now that you know so many move types, you'll maybe have noticed how some move types are very picky when it comes to possible states. This one, thankfully, isn't. ")
        print(f"Might be a bit tricky at first: {self.current}. GO!")

    def validate(self, i, sign): #validates for extremes - sign flip move type
        if i < 0 or i >= self.length:
            return "oob_error"
        return "no_error"

    def permute(self, i, sign): #extremes - sign flip move type
        l = self.length
        if sign == "+":
           self.current.insert(l,-self.current.pop(i))
        else:
            self.current.insert(0,-self.current.pop(i))
            