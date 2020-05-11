__author__ = 'Sophia Gold'

from GP.fitness import fitness
import random

# this will try to have the generated code give back float x at some mark
# the code executed would mutate and switch simple functions

# the environment the code will be run in that will determine the fitness
# the higher the fitness the better
class environment:
    def __init__(self):
        self.target = random.random()

    def evaluate(self, chrom):
        self.x = 1
        # run the chromosome code
        exec(chrom, locals())
        try:
            return 1/abs(self.x-self.target)
        except:
            return 10000000


seedCode = [
    "self.x = 1.1\nself.x = self.x/1.8\nself.x += .1\nself.x +=.1",
    "self.x = 2.2\nself.x -= .1\nself.x +=.1\nself.x +=.1",
    "self.x += self.x*1.1\nself.x = self.x/3.5\nself.x += self.x*2\nself.x +=2.3",
    "self.x = 1.5\nself.x = self.x/4\nself.x += self.x*2.1\nself.x +=.1",
    "self.x = 11\nself.x = self.x/3\nself.x += self.x*2\nself.x +=1.1",
    "self.x = 1\nself.x = self.x/2\nself.x += self.x*1.1\nself.x +=2.1",
    "self.x = 1\nself.x = self.x/3.2\nself.x += self.x*2.1\nself.x +=.14",
    "self.x += self.x*1.1\nself.x = self.x/4.1\nself.x += self.x*3.1\nself.x +=.1",
    "self.x = 2.1\nself.x = self.x/3.1\nself.x += self.x*2.1\nself.x +=.16",
    "self.x += self.x*1.11\nself.x = self.x/2.5\nself.x += self.x*4.1\nself.x -=1.19"
]

if __name__ == '__main__':
    # run seedCode through fitness loop
    print("start")
    fit = fitness()
    fit.runGP(seedCode, environment)
