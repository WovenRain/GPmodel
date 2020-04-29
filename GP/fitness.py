__author__ = 'Sophia Gold'

from GP import crossover
from datetime import datetime
import os

# put string into fitness environment

def runGP(self, gen, environment,
          destination = "GPRun",
          cSettings = crossover(),
          targetFitness = 10000000):

    # lots of things to go wrong
    try:
        # put the date and time on the generated folder
        destination += datetime.now()
        try:
            os.mkdir(destination)
        except:
            print("problem making directory")
            # already a dir?

        # start gp loop
        fitnessLoop = 0
        while True:
            print("Generation " + str(fitnessLoop))

            # create generation dir
            try:
                os.mkdir(destination + "/gen " + str(fitnessLoop))
            except:
                print("problem making gen " + str(fitnessLoop) + " directory")

            genFitness = []
            i = 0
            while i < len(gen):
                # get fitness of gene and output
                f = environment.evaluate(gen[i])
                genFitness.append(f)
                print("C" + str(i) + " fitness: " + str(f))

                # save file
                fileOutput = open(destination + "/" + str(f) + ".py", 'w')
                fileOutput.write(gen[i])
                fileOutput.close()

                i += 1

            # check completion
            if max(genFitness) >= targetFitness:
                print("Solution found ending")
                break

            # create new generation
            gen = cSettings.cross(gen, genFitness)
            fitnessLoop += 1

    except:
        print("something went wrong DX")
