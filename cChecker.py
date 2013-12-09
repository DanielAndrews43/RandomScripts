#Checks if it's more effective to only bubble in C's or bubble randomly
class cChecker(object):
    def __init__(self,amount):
        self.amount = amount
        self.test = self.createTest(amount)
    def createTest(self,amount):
        from random import random
        test = []
        for i in range(amount):
            num = int(random()*4)
            test.append(num)
    def checkC(self,test):
        correct = 0
        for i in test:
            if i == 3:
                correct += 1
        return correct
    def checkRandom(self,test):
        from random import random
        correct = 0
        for i in test:
            num = int(random()*4)
            if num == i:
                correct += 1
        return correct
    def wrapper(self):
        c = self.checkC(self.test).correct
        random = self.cehckRandom(self.test).correct
        print ('Only bubbling c is ' 'better' if c>random else 'worse' 
                ' than bubbling randomly')
        
