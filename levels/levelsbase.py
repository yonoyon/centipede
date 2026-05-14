import time

class LevelsBase:
    
    def __init__(self, commands):
        self.commands = commands
        self.input_yes = {
        "yes" : self.y,
        "y" : self.y,
        "yeah" : self.y,
        "ye" : self.y,
        "yea" : self.y,
        "okay" : self.y,
        "continue" : self.y
        }
        self.solved = []
        self.scrambled = []
        self.current = []
        self.length = len(self.solved)
        #solved states for levels below (number indicates length)
        self.solved_6 = list(range(1, 7))
        self.solved_8 = list(range(1, 9))
        self.solved_10 = list(range(1, 11))

    def y(self): #a bit unnecessary but whatevs
        print("Continuing...")
        time.sleep(1)

    def play_level(self): #main loop for any level
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

    def level_end(self): #called when user finishes level
        while True:
            user_input = input("Would you like to try again? Input: ").strip().lower()
            if  user_input in self.input_yes:
                self.input_yes[user_input]()
                return True
            elif user_input in self.commands:
                self.commands[user_input]()
            else:
                return False

    def get_move(self): #gets move from user, calls parse_move and validate (level specific) to filter out bad move notation/illegal moves
        while True:
            move = input("Input move: ")
            if move in self.commands:
                self.commands[move]()
                continue
            try:
                i, sign = self.parse_move(move)
            except ValueError as e:
                print(f"Invalid move; {e}")
                continue
            if self.validate(i, sign):
                return i, sign
        
    def parse_move(self, move): #see get_move()
        if len(move) < 2:
            raise ValueError("Too short (move must consist of direction and position). ")

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
