import time

from ..levelsmode import LevelsMode

class Level_1(LevelsMode):

    def __init__(self,commands,available_levels):
        #super().__init__(commands)
        self.available_levels  = available_levels
        #self.solved = self.solved_6.copy()
        self.scrambled = [1, 3, 2, 5, 6, 4]
    
    def run(self):
        self.start(self.scrambled)
        if 2 not in self.available_levels:
            self.available_levels.append(2)
        return False

    def welcome(self):
        print("Welcome to level 1. The goal of any level is to permute the given centipede into a solved state. ")
        time.sleep(1)
        print("A solved state will always look the same: positive numbers from 1 upward. ")
        time.sleep(1)
        print(f"Have a try with {self.scrambled} - you can almost certainly solve this intuitively. Input help if you don't know the move notation, or if you need help in general. ")
        print("Have fun!")  
