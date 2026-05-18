from .levelslogic import LevelsLogic
from .levelsbase import LevelsBase

class LevelsMode():
    
    def __init__(self):
        pass

    def start(self, scramble):
        while True:
            base = LevelsBase()
            logic = LevelsLogic()
            
            
            move = base.get_move()
            result = logic.play()#move, scramble)
            
            if result is True:
                if base.finish():
                    print("hi")
                    continue
                else:
                    break
            

