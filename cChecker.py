#Checks if it's more effective to only bubble in C's or bubble randomly
class cChecker(object):
    def __init__(self,amount):
        self.test = self.createTest(amount)
    def createTest(self,amount):
        from random import random
        test = []
        for i in range(amount):
            num = int(random()*4)
            test.append(num)
        return test
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
    def checkTest(self):
        zero = 0
        one = 0
        two = 0
        three = 0
        for i in self.test:
            if i == 0:
                zero += 1
            elif i == 1:
                one += 1
            elif i == 2:
                two += 1
            else:
                three += 1
        print zero
        print one
        print two
        print three
    def wrapper(self):
        c = self.checkC(self.test)
        random = self.checkRandom(self.test)
        print ('Only bubbling c is ' + ('better' if c>random else 'worse') + 
                ' than bubbling randomly')

def checkBetter(times):
    for i in xrange(times):
        foo = cChecker(1000)
        print foo.wrapper()

checkBetter(10)
#End result: Makes absolutely no difference...
    