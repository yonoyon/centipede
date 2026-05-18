

class LevelsLogic():


    def __init__(self):
        pass

    def play(self):
            return True
    
    def get_move(self): #gets move from user, calls parse_move and validate (level specific) to filter out bad move notation/illegal moves LOGIC
        while True:
            move = self.input_move()
            if self.check_for_commands(move):
                continue
            try:
                i, sign = self.parse_move(move)
            except ValueError as e:
                self.print_invalid_move(e)
                continue
            
            error = self.validate(i, sign)

            if error == "no_error":
                return i, sign

            if error in self.illegal_moves:
                self.print_illegal_move(error)
                continue

    def parse_move(self, move): #see get_move() LOGIC
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

    def check(self): #LOGIC
        return self.current == self.solved

    def check_for_commands(self, thing): #LOGIC
        if thing in self.commands:
            self.commands[thing]()
            return True

    def logic_play_level(self): #main loop for any level LOGIC
        x = 0
        while True:
            self.print_current_state()
            i, sign = self.get_move()
            self.permute(i, sign)
            x+=1
            if self.check():
                if x > 1:
                    self.print_move_count(x, 1)
                if x == 1:
                    self.print_move_count(x, 0)
                if self.level_end():
                    x = 0
                    self.current = self.scrambled.copy()
                    continue
                else:
                    return False

    def level_end(self): #called when user finishes level LOGIC
        while True:
            user_input = self.input_level_end()
            if  user_input in self.input_yes:
                self.input_yes[user_input]()
                return True
            elif user_input in self.commands:
                self.commands[user_input]()
            else:
                return False

        