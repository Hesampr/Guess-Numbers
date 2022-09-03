from random import randint as ri


#guess number class
class Guess:
    number = int()
    def __init__(self,number1,number2):
        self.number = ri(number1,number2+1)
        
    def CheckTrue(self,n2):
        if self.number==n2:
            return True
        else:
            return False


