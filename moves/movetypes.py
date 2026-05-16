class MoveTypes():
    
    def __init__(self):
        pass
    def validate(self, i, sign, current):
        raise NotImplementedError

    def permute(self, i, sign, current):
        raise NotImplementedError

class AS(MoveTypes): #adjacent swap
    
    def validate(self, i, sign, current):
        if i < 0 or i >= len(current):
            return "oob_error"
        if sign == "+" and i + 1 >= len(current):
            return "right_impossible_error"
        if sign == "-" and i - 1 < 0:
            return "left_impossible_error"
        return "no_error"

    def permute(self, i, sign, current):
        if sign == "+":
            current[i], current[i+1] = current[i+1], current[i]
        else:
            current[i], current[i-1] = current[i-1], current[i]

class ASSF(MoveTypes): #adjacent swap - sign flip
    
    def validate(self, i, sign, current):
        if i < 0 or i >= len(current):
            return "oob_error"
        if sign == "+" and i + 1 >= len(current):
            return "right_impossible_error"
        if sign == "-" and i - 1 < 0:
            return "left_impossible_error"
        return "no_error"

    def permute(self, i, sign, current):
        if sign == "+":
            current[i], current[i+1] = -current[i+1], -current[i]
        else:
            current[i], current[i-1] = -current[i-1], -current[i]

class EX(MoveTypes): #extremes
    
    def validate(self, i, sign, current):
        if i < 0 or i >= len(current):
            return "oob_error"
        return "no_error"

    def permute(self, i, sign, current):
        l = len(current)
        if sign == "+":
           current.insert(l,current.pop(i))
        else:
            current.insert(0,current.pop(i))

class EXSF(MoveTypes): #extremes - sign flip
    
    def validate(self, i, sign, current):
        if i < 0 or i >= len(current):
            return "oob_error"
        return "no_error"

    def permute(self, i, sign, current):
        l = len(current)
        if sign == "+":
           current.insert(l,-current.pop(i))
        else:
            current.insert(0,-current.pop(i))

class JS(MoveTypes): #jump swap
    
    def validate(self, i, sign, current):
        if i < 0 or i >= len(current):
            return "oob_error"
        if sign == "+" and i + 2 >= len(current):
            return "right_impossible_error"
        if sign == "-" and i - 2 < 0:
            return "left_impossible_error"
        return "no_error"

    def permute(self, i, sign, current):
        if sign == "+":
            current[i], current[i+2] = current[i+2], current[i]
        else:
            current[i], current[i-2] = current[i-2], current[i]

class JSSF(MoveTypes): #jump swap - sign flip
    def validate(self, i, sign, current):
        if i < 0 or i >= len(current):
            return "oob_error"
        if sign == "+" and i + 2 >= len(current):
            return "right_impossible_error"
        if sign == "-" and i - 2 < 0:
            return "left_impossible_error"
        return "no_error"

    def permute(self, i, sign, current):
        if sign == "+":
            current[i], current[i+2] = -current[i+2], -current[i]
        else:
            current[i], current[i-2] = -current[i-2], -current[i]