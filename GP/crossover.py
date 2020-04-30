__author__ = 'Sophia Gold'

import numpy
import random
class crossover:
    def __init__(self):
        # if generation is odd size the bottom will always be dropped off
        # only implementing simplest for now
        self.crossoverType = {
            "SinglePC": 0,
            "TwoPC": 1
        }

        # each selection type will return 2 lists,
        # both the size of the original, organised in some way for control of generation size
        # which is checked at the end of each crossover method
        self.selectionType = {
            "EvenOdd": 0,
            "BestHalf": 1
        }

        self.settings()

    @staticmethod
    def evenodd(generation, ranked):
        even = False
        list1 = []
        list2 = []
        i = 0
        while i < len(generation):
            if even:
                list1.append(generation[ranked[i]])
                even = False
            else:
                list2.append(generation[ranked[i]])
                even = True
            i += 1
        return [list1, list2]

    @staticmethod
    def splitter(codeStr):
        # split the code into a list of strings by line
        return codeStr.split("\n")
    @staticmethod
    def fixer(stringList):
        return "\n".join(stringList)

    def settings(self,
                 generation_size = -1,
                 crossover_type = "SinglePC",
                 selection_type = "EvenOdd",
                 mut = 0.05):
        # default crossover type, selection, and mutation rate
        self.cType = self.crossoverType[crossover_type]
        self.cSelection = self.selectionType[selection_type]
        self.mutationRate = mut
        self.generationSize = generation_size

    def singlepc(self, side1, side2):
        newGen = []
        # run through first half of lists
        i = 0
        while len(newGen) < self.generationSize:
            # get both split strings
            parentA = self.splitter(side1[i])
            parentB = self.splitter(side2[i])

            # cross over somewhere in the middle, by line number
            if len(parentA) > len(parentB):
                lines = len(parentA)
            elif len(parentA) < len(parentB):
                lines = len(parentB)
            else:
                lines = len(parentA)
            splitAt = random.randint(1, lines)

            # put 1 in reserve location,
            reserve = parentA

            # put 2 in 1s place
            j = splitAt
            while j < lines:
                parentA[j] = parentB[j]
                j += 1

            # put reserve in 2
            j = splitAt
            while j < lines:
                parentB[j] = reserve[j]
                j += 1

            # add altered parents to newGen
            newGen.append(self.fixer(parentA))
            newGen.append(self.fixer(parentB))
            i += 1
        return newGen

    def cross(self, generation, genFitness):
        #set the size of the generation
        if self.generationSize == -1:
            self.generationSize = len(generation)

        # get the sorted list
        rank = numpy.argsort(genFitness)
        # put best scorers first
        ranked = []
        i = 0
        while i < len(rank):
            i += 1
            ranked.append(rank[len(rank)-i])

        # get 2 lists of chromosomes to cross against each other
        lists = []
        newGen = []
        if self.cSelection == 0:
            lists = self.evenodd(generation, ranked)
        # elif self.cSelection == 1:

        # Do crossover in sorted lists
        if self.cType == 0:
            newGen = self.singlepc(lists[0], lists[1])
        # elif self.cType == 1:

        #mutate then return newGen
        return newGen
