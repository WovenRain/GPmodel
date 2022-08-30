__author__ = 'Sophia Gold'

from GP.fitness import fitness
from GP.crossover import crossover
import random

# this will try to have the generated code give back float x at some mark
# the code executed would mutate and switch simple functions

# the environment the code will be run in that will determine the fitness
# the higher the fitness the better
class environment:
    def __init__(self):
        self.target = random.random()
        # self.target = 6.16161616

    def evaluate(self, chrom):
        self.x = 1
        # run the chromosome code
        exec(chrom, locals())
        print(self.x)
        try:
            return 1/abs(self.x-self.target)
        except:
            return 0


seedCode = [
    "self.x = 1.1\nself.x = self.x/1.8\nself.x += .741\nself.x +=.1\nself.x = self.x/4\nself.x += self.x*2.1",
    "self.x = 2.2\nself.x -= .1\nself.x +=.1\nself.x +=.1111\nself.x = self.x/1.8\nself.x += .741",
    "self.x += self.x*1.1\nself.x = self.x/3.5\nself.x += self.x*2\nself.x +=2.3\nself.x = self.x/4\nself.x += self.x*2.1",
    "self.x = 1.5\nself.x = self.x/4\nself.x += self.x*2.1\nself.x +=.1\nself.x = self.x/1.8\nself.x += .741",
    "self.x = 11\nself.x = self.x/3\nself.x += self.x*2\nself.x +=1.1\nself.x = self.x/4\nself.x += self.x*2.1",
    "self.x = 10\nself.x = self.x/2\nself.x += self.x*1.1631\nself.x +=2.1\nself.x = self.x/1.8\nself.x += .741",
    "self.x = 1\nself.x = self.x/3.2\nself.x += self.x*2.1\nself.x +=.14\nself.x = self.x/4\nself.x += self.x*2.1",
    "self.x += self.x*1.1\nself.x = self.x/4.1\nself.x += self.x*3.1\nself.x +=.1\nself.x = self.x/1.8\nself.x += .741",
    "self.x = 2.1\nself.x = self.x/3.1\nself.x += self.x*2.1\nself.x +=.168\nself.x = self.x/4\nself.x += self.x*2.1",
    "self.x += self.x*1.11\nself.x = self.x/2.5\nself.x += self.x*4.1\nself.x -=1.19\nself.x = self.x/4\nself.x += self.x*2.1",
    "self.x = 1.1\nself.x = self.x/1.8\nself.x += .741\nself.x +=.1\nself.x = self.x/1.8\nself.x += .741",
    "self.x = 2.2\nself.x -= .1\nself.x +=.1\nself.x +=.1111\nself.x = self.x/4\nself.x += self.x*2.1",
    "self.x += self.x*1.1\nself.x = self.x/3.5\nself.x += self.x*2\nself.x +=2.3\nself.x = self.x/1.8\nself.x += .741",
    "self.x = 1.5\nself.x = self.x/4\nself.x += self.x*2.1\nself.x +=.1\nself.x = self.x/4\nself.x += self.x*2.1",
    "self.x = 11\nself.x = self.x/3\nself.x += self.x*2\nself.x +=1.1\nself.x = self.x/1.8\nself.x += .741",
    "self.x = 10\nself.x = self.x/2\nself.x += self.x*1.1631\nself.x +=2.1\nself.x = self.x/4\nself.x += self.x*2.1",
    "self.x = 1\nself.x = self.x/3.2\nself.x += self.x*2.1\nself.x +=.14\nself.x = self.x/1.8\nself.x += .741",
    "self.x += self.x*1.1\nself.x = self.x/4.1\nself.x += self.x*3.1\nself.x +=.1\nself.x = self.x/4\nself.x += self.x*2.1",
    "self.x = 2.1\nself.x = self.x/3.1\nself.x += self.x*2.1\nself.x +=.168\nself.x = self.x/1.8\nself.x += .741",
    "self.x += self.x*1.11\nself.x = self.x/2.5\nself.x += self.x*4.1\nself.x -=1.19\nself.x = self.x/4\nself.x += self.x*2.1",
    "self.x = 1.1\nself.x = self.x/1.8\nself.x += .741\nself.x +=.1\nself.x = self.x/4\nself.x += self.x*2.1",
    "self.x = 2.2\nself.x -= .1\nself.x +=.1\nself.x +=.1111\nself.x = self.x/1.8\nself.x += .741",
    "self.x += self.x*1.1\nself.x = self.x/3.5\nself.x += self.x*2\nself.x +=2.3\nself.x = self.x/4\nself.x += self.x*2.1",
    "self.x = 1.5\nself.x = self.x/4\nself.x += self.x*2.1\nself.x +=.1\nself.x = self.x/1.8\nself.x += .741",
    "self.x = 11\nself.x = self.x/3\nself.x += self.x*2\nself.x +=1.1\nself.x = self.x/4\nself.x += self.x*2.1",
    "self.x = 10\nself.x = self.x/2\nself.x += self.x*1.1631\nself.x +=2.1\nself.x = self.x/1.8\nself.x += .741",
    "self.x = 1\nself.x = self.x/3.2\nself.x += self.x*2.1\nself.x +=.14\nself.x = self.x/4\nself.x += self.x*2.1",
    "self.x += self.x*1.1\nself.x = self.x/4.1\nself.x += self.x*3.1\nself.x +=.1\nself.x = self.x/1.8\nself.x += .741",
    "self.x = 2.1\nself.x = self.x/3.1\nself.x += self.x*2.1\nself.x +=.168\nself.x = self.x/4\nself.x += self.x*2.1",
    "self.x += self.x*1.11\nself.x = self.x/2.5\nself.x += self.x*4.1\nself.x -=1.19\nself.x = self.x/4\nself.x += self.x*2.1",
    "self.x = 1.1\nself.x = self.x/1.8\nself.x += .741\nself.x +=.1\nself.x = self.x/1.8\nself.x += .741",
    "self.x = 2.2\nself.x -= .1\nself.x +=.1\nself.x +=.1111\nself.x = self.x/4\nself.x += self.x*2.1",
    "self.x += self.x*1.1\nself.x = self.x/3.5\nself.x += self.x*2\nself.x +=2.3\nself.x = self.x/1.8\nself.x += .741",
    "self.x = 1.5\nself.x = self.x/4\nself.x += self.x*2.1\nself.x +=.1\nself.x = self.x/4\nself.x += self.x*2.1",
    "self.x = 11\nself.x = self.x/3\nself.x += self.x*2\nself.x +=1.1\nself.x = self.x/1.8\nself.x += .741",
    "self.x = 10\nself.x = self.x/2\nself.x += self.x*1.1631\nself.x +=2.1\nself.x = self.x/4\nself.x += self.x*2.1",
    "self.x = 1\nself.x = self.x/3.2\nself.x += self.x*2.1\nself.x +=.14\nself.x = self.x/1.8\nself.x += .741",
    "self.x += self.x*1.1\nself.x = self.x/4.1\nself.x += self.x*3.1\nself.x +=.1\nself.x = self.x/4\nself.x += self.x*2.1",
    "self.x = 2.1\nself.x = self.x/3.1\nself.x += self.x*2.1\nself.x +=.168\nself.x = self.x/1.8\nself.x += .741",
    "self.x += self.x*1.11\nself.x = self.x/2.5\nself.x += self.x*4.1\nself.x -=1.19\nself.x = self.x/4\nself.x += self.x*2.1",
    "self.x = 1.1\nself.x = self.x/1.8\nself.x += .741\nself.x +=.1\nself.x = self.x/4\nself.x += self.x*2.1",
    "self.x = 2.2\nself.x -= .1\nself.x +=.1\nself.x +=.1111\nself.x = self.x/1.8\nself.x += .741",
    "self.x += self.x*1.1\nself.x = self.x/3.5\nself.x += self.x*2\nself.x +=2.3\nself.x = self.x/4\nself.x += self.x*2.1",
    "self.x = 1.5\nself.x = self.x/4\nself.x += self.x*2.1\nself.x +=.1\nself.x = self.x/1.8\nself.x += .741",
    "self.x = 11\nself.x = self.x/3\nself.x += self.x*2\nself.x +=1.1\nself.x = self.x/4\nself.x += self.x*2.1",
    "self.x = 10\nself.x = self.x/2\nself.x += self.x*1.1631\nself.x +=2.1\nself.x = self.x/1.8\nself.x += .741",
    "self.x = 1\nself.x = self.x/3.2\nself.x += self.x*2.1\nself.x +=.14\nself.x = self.x/4\nself.x += self.x*2.1",
    "self.x += self.x*1.1\nself.x = self.x/4.1\nself.x += self.x*3.1\nself.x +=.1\nself.x = self.x/1.8\nself.x += .741",
    "self.x = 2.1\nself.x = self.x/3.1\nself.x += self.x*2.1\nself.x +=.168\nself.x = self.x/4\nself.x += self.x*2.1",
    "self.x += self.x*1.11\nself.x = self.x/2.5\nself.x += self.x*4.1\nself.x -=1.19\nself.x = self.x/4\nself.x += self.x*2.1",
    "self.x = 1.1\nself.x = self.x/1.8\nself.x += .741\nself.x +=.1\nself.x = self.x/1.8\nself.x += .741",
    "self.x = 2.2\nself.x -= .1\nself.x +=.1\nself.x +=.1111\nself.x = self.x/4\nself.x += self.x*2.1",
    "self.x += self.x*1.1\nself.x = self.x/3.5\nself.x += self.x*2\nself.x +=2.3\nself.x = self.x/1.8\nself.x += .741",
    "self.x = 1.5\nself.x = self.x/4\nself.x += self.x*2.1\nself.x +=.1\nself.x = self.x/4\nself.x += self.x*2.1",
    "self.x = 11\nself.x = self.x/3\nself.x += self.x*2\nself.x +=1.1\nself.x = self.x/1.8\nself.x += .741",
    "self.x = 10\nself.x = self.x/2\nself.x += self.x*1.1631\nself.x +=2.1\nself.x = self.x/4\nself.x += self.x*2.1",
    "self.x = 1\nself.x = self.x/3.2\nself.x += self.x*2.1\nself.x +=.14\nself.x = self.x/1.8\nself.x += .741",
    "self.x += self.x*1.1\nself.x = self.x/4.1\nself.x += self.x*3.1\nself.x +=.1\nself.x = self.x/4\nself.x += self.x*2.1",
    "self.x = 2.1\nself.x = self.x/3.1\nself.x += self.x*2.1\nself.x +=.168\nself.x = self.x/1.8\nself.x += .741",
    "self.x += self.x*1.11\nself.x = self.x/2.5\nself.x += self.x*4.1\nself.x -=1.19\nself.x = self.x/4\nself.x += self.x*2.1",
    "self.x = 1.1\nself.x = self.x/1.8\nself.x += .741\nself.x +=.1\nself.x = self.x/4\nself.x += self.x*2.1",
    "self.x = 2.2\nself.x -= .1\nself.x +=.1\nself.x +=.1111\nself.x = self.x/1.8\nself.x += .741",
    "self.x += self.x*1.1\nself.x = self.x/3.5\nself.x += self.x*2\nself.x +=2.3\nself.x = self.x/4\nself.x += self.x*2.1",
    "self.x = 1.5\nself.x = self.x/4\nself.x += self.x*2.1\nself.x +=.1\nself.x = self.x/1.8\nself.x += .741",
    "self.x = 11\nself.x = self.x/3\nself.x += self.x*2\nself.x +=1.1\nself.x = self.x/4\nself.x += self.x*2.1",
    "self.x = 10\nself.x = self.x/2\nself.x += self.x*1.1631\nself.x +=2.1\nself.x = self.x/1.8\nself.x += .741",
    "self.x = 1\nself.x = self.x/3.2\nself.x += self.x*2.1\nself.x +=.14\nself.x = self.x/4\nself.x += self.x*2.1",
    "self.x += self.x*1.1\nself.x = self.x/4.1\nself.x += self.x*3.1\nself.x +=.1\nself.x = self.x/1.8\nself.x += .741",
    "self.x = 2.1\nself.x = self.x/3.1\nself.x += self.x*2.1\nself.x +=.168\nself.x = self.x/4\nself.x += self.x*2.1",
    "self.x += self.x*1.11\nself.x = self.x/2.5\nself.x += self.x*4.1\nself.x -=1.19\nself.x = self.x/4\nself.x += self.x*2.1",
    "self.x = 1.1\nself.x = self.x/1.8\nself.x += .741\nself.x +=.1\nself.x = self.x/1.8\nself.x += .741",
    "self.x = 2.2\nself.x -= .1\nself.x +=.1\nself.x +=.1111\nself.x = self.x/4\nself.x += self.x*2.1",
    "self.x += self.x*1.1\nself.x = self.x/3.5\nself.x += self.x*2\nself.x +=2.3\nself.x = self.x/1.8\nself.x += .741",
    "self.x = 1.5\nself.x = self.x/4\nself.x += self.x*2.1\nself.x +=.1\nself.x = self.x/4\nself.x += self.x*2.1",
    "self.x = 11\nself.x = self.x/3\nself.x += self.x*2\nself.x +=1.1\nself.x = self.x/1.8\nself.x += .741",
    "self.x = 10\nself.x = self.x/2\nself.x += self.x*1.1631\nself.x +=2.1\nself.x = self.x/4\nself.x += self.x*2.1",
    "self.x = 1\nself.x = self.x/3.2\nself.x += self.x*2.1\nself.x +=.14\nself.x = self.x/1.8\nself.x += .741",
    "self.x += self.x*1.1\nself.x = self.x/4.1\nself.x += self.x*3.1\nself.x +=.1\nself.x = self.x/4\nself.x += self.x*2.1",
    "self.x = 2.1\nself.x = self.x/3.1\nself.x += self.x*2.1\nself.x +=.168\nself.x = self.x/1.8\nself.x += .741",
    "self.x += self.x*1.11\nself.x = self.x/2.5\nself.x += self.x*4.1\nself.x -=1.19\nself.x = self.x/4\nself.x += self.x*2.1",
    "self.x = 1.1\nself.x = self.x/1.8\nself.x += .741\nself.x +=.1\nself.x = self.x/4\nself.x += self.x*2.1",
    "self.x = 2.2\nself.x -= .1\nself.x +=.1\nself.x +=.1111\nself.x = self.x/1.8\nself.x += .741",
    "self.x += self.x*1.1\nself.x = self.x/3.5\nself.x += self.x*2\nself.x +=2.3\nself.x = self.x/4\nself.x += self.x*2.1",
    "self.x = 1.5\nself.x = self.x/4\nself.x += self.x*2.1\nself.x +=.1\nself.x = self.x/1.8\nself.x += .741",
    "self.x = 11\nself.x = self.x/3\nself.x += self.x*2\nself.x +=1.1\nself.x = self.x/4\nself.x += self.x*2.1",
    "self.x = 10\nself.x = self.x/2\nself.x += self.x*1.1631\nself.x +=2.1\nself.x = self.x/1.8\nself.x += .741",
    "self.x = 1\nself.x = self.x/3.2\nself.x += self.x*2.1\nself.x +=.14\nself.x = self.x/4\nself.x += self.x*2.1",
    "self.x += self.x*1.1\nself.x = self.x/4.1\nself.x += self.x*3.1\nself.x +=.1\nself.x = self.x/1.8\nself.x += .741",
    "self.x = 2.1\nself.x = self.x/3.1\nself.x += self.x*2.1\nself.x +=.168\nself.x = self.x/4\nself.x += self.x*2.1",
    "self.x += self.x*1.11\nself.x = self.x/2.5\nself.x += self.x*4.1\nself.x -=1.19\nself.x = self.x/4\nself.x += self.x*2.1",
    "self.x = 1.1\nself.x = self.x/1.8\nself.x += .741\nself.x +=.1\nself.x = self.x/1.8\nself.x += .741",
    "self.x = 2.2\nself.x -= .1\nself.x +=.1\nself.x +=.1111\nself.x = self.x/4\nself.x += self.x*2.1",
    "self.x += self.x*1.1\nself.x = self.x/3.5\nself.x += self.x*2\nself.x +=2.3\nself.x = self.x/1.8\nself.x += .741",
    "self.x = 1.5\nself.x = self.x/4\nself.x += self.x*2.1\nself.x +=.1\nself.x = self.x/4\nself.x += self.x*2.1",
    "self.x = 11\nself.x = self.x/3\nself.x += self.x*2\nself.x +=1.1\nself.x = self.x/1.8\nself.x += .741",
    "self.x = 10\nself.x = self.x/2\nself.x += self.x*1.1631\nself.x +=2.1\nself.x = self.x/4\nself.x += self.x*2.1",
    "self.x = 1\nself.x = self.x/3.2\nself.x += self.x*2.1\nself.x +=.14\nself.x = self.x/1.8\nself.x += .741",
    "self.x += self.x*1.1\nself.x = self.x/4.1\nself.x += self.x*3.1\nself.x +=.1\nself.x = self.x/4\nself.x += self.x*2.1",
    "self.x = 2.1\nself.x = self.x/3.1\nself.x += self.x*2.1\nself.x +=.168\nself.x = self.x/1.8\nself.x += .741",
    "self.x += self.x*1.11\nself.x = self.x/2.5\nself.x += self.x*4.1\nself.x -=1.19\nself.x = self.x/4\nself.x += self.x*2.1"
]

if __name__ == '__main__':
    # run seedCode through fitness loop
    fit = fitness()
    fit.runGP(seedCode, environment)
    #fit.runGP(seedCode, environment, savePath, crossoverSettings, saveThreshold, solutionLimit, NumberOfGenerations)
    #fit.runGP(seedCode, environment, "6.16161616 ", crossover, 10.0, 10000, 1000)
