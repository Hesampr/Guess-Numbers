from random import randint as ri


#guess number class
class Guess:
    number = int()
    def __init__(self,period):
        number1=1
        self.number = ri(number1,period+1)
        
    def CheckTrue(self,n2):
        if self.number==n2:
            return True
        else:
            return False


