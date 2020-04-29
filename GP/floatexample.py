__author__ = 'Sophia Gold'

from GP import crossover, fitness

# this will try to have the generated code give back float x at some mark
# the code executed would mutate and switch simple functions

# the environment the code will be run in that will determine the fitness
# the higher the fitness the better
class environment:
    def evaluate(self, chrom):
        x = 0
        # run the chromosome code
        exec(chrom)
        try:
            return 1.0/(x - 3.141592).abs()
        except:
            # wanting to divide by zero, the goal has been found
            # messy but does the job
            return 100000000


seedCode = [
    "x = 1.1\nx = x/2 \nx += .1",
    "x = 2.2\nx -= .1",
    "x = 1.1\nx +=.1",
    "x = 1.1\nwhile(x < 4):\n   x = x*3\n   x -= 1.4"
]

if __name__ == '__main__':
    # run seedCode through fitness loop
    fitness.runGP(seedCode, environment)
