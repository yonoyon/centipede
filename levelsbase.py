import time

class Levelsbase:
    
    def __init__(self, commands):
        self.commands = commands
        self.solved = []
        self.scrambled = []
        self.current = []
        self.length = len(self.solved)

    def play_level(self):
        x = 0
        while True:
            print(f"Current state: {self.current}")
            i, sign = self.get_move()
            self.permute(i, sign)
            x+=1
            if self.check():
                if x > 1:
                    print(f"Congratulations! You solved it in {x} moves!")
                if x == 1:
                    print(f"Congratulations! You solved it in {x} move!")
                if self.level_end():
                    x = 0
                    self.current = self.scrambled.copy()
                    continue
                else:
                    return False
        return True

    def level_end(self):
        while True:
            user_input = input("Would you like to try again? Input: ").strip().lower()
            if  user_input == "yes":
                time.sleep(1)
                return True
            elif user_input in self.commands:
                self.commands[user_input]()
            else:
                return False

    def get_move(self):
        while True:
            move = input("Input move: ")
            try:
                i, sign = self.parse_move(move)
            except ValueError as e:
                print(f"Invalid move; {e}")
                continue
            if self.validate(i, sign):
                return i, sign
            else:
                print("Illegal move. ")
        
    def parse_move(self, move):
        if len(move) < 2:
            raise ValueError("Too short. ")

        try:
            i = int(move[:-1]) - 1
        except ValueError: 
            raise ValueError("Not a valid position. ")
        
        sign = move[-1]
        if sign not in "+-":
            raise ValueError("Not a valid direction. ")
    
        return i, sign

    def check(self):
        return self.current == self.solved
