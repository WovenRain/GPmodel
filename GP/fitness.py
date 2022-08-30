__author__ = 'Sophia Gold'

from GP.crossover import crossover
from datetime import datetime
import os

class fitness:

    def runGP(self, gen, environment,
              destination = "GPRun ",
              cSettings = crossover,
              minFitnessToSave = 10.0,
              targetFitness = 10000000,
              generationRoundLimit = 1000):
        # put the date and time on the generated folder
        destination += str(datetime.now())
        destination = destination.replace(":", "")
        try:
            os.mkdir(destination)
        except Exception as e:
            print(e.with_traceback())
            # already a dir?

        # start gp loop
        fitnessLoop = 0
        e = environment()
        c = cSettings()
        while True:
            print("Generation " + str(fitnessLoop))
            genFitness = []
            i = 0
            while i < len(gen):
                # get fitness of gene and output
                try:
                    f = e.evaluate(chrom = gen[i])
                except Exception as e:
                    # try to fix by the problem using e

                    # if it doesnt fix then fail the chromosome
                    # also stop from spending too much time on this

                    print("Failed to Evaluate " + str(e))
                    f = 0

                genFitness.append(f)
                print("C" + str(i) + " fitness: " + str(f))

                # save file if over minimum fitness to save value
                if f >= minFitnessToSave:
                    fileOutput = open(destination + "/" + str(f) + ".py", 'w')
                    fileOutput.write(gen[i])
                    fileOutput.close()

                i += 1

            print("Average fitness: " + str(sum(genFitness)/len(genFitness)))
            # check completion
            if max(genFitness) >= targetFitness:
                print("Solution found ending")
                break
            fitnessLoop += 1
            if fitnessLoop >= generationRoundLimit:
                break

            # create new generation
            gen = c.cross(generation=gen, genFitness = genFitness)
