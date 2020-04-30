__author__ = 'Sophia Gold'

from GP.fitness import fitness

# this will try to have the generated code give back float x at some mark
# the code executed would mutate and switch simple functions

# the environment the code will be run in that will determine the fitness
# the higher the fitness the better
class environment:
    @staticmethod
    def evaluate(chrom):
        x = 1
        # run the chromosome code
        exec(chrom)
        print(x)
        try:
            return 1/abs(x-3.141592)
        except:
            return 10000000


seedCode = [
    "x = 1.1\nx = x/2 \nx += .1\nx +=.1",
    "x = 2.2\nx -= .1\nx +=.1\nx +=.1",
    "x = 1.1\nx = x/3\nx += x*2.1\nx +=.1",
    "x = 1.1\nx = x/3\nx += x*3.1\nx -=.1"
    # "x = 1.1\nwhile(x < 4):\n   x = x*3\n   x -= 1.4"
]

if __name__ == '__main__':
    # run seedCode through fitness loop
    print("start")
    fit = fitness()
    fit.runGP(seedCode, environment)
