__author__ = 'Sophia Gold'

import numpy

# if generation is odd size the bottom will always be dropped off
# only implementing simplest for now

crossoverType = {
    "SinglePC": 0,
    "TwoPC": 1
}
selectionType = {
    "EvenOdd": 0,
    "BestHalf": 1
}

def settings(self,
             crossover_type = "SinglePC",
             selection_type = "EvenOdd",
             mut = 0.05):
    # default crossover type, selection, and mutation rate
    self.cType = crossoverType[crossover_type]
    self.cSelection = selectionType[selection_type]
    self.mutationRate = mut

def singlepc(self, side1, side2):

def evenodd(self, generation, ranked):
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

def cross(self, generation, genFitness):
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
    if self.cSelection == 0:
        lists = evenodd(generation, ranked)
    # elif self.cSelection == 1:

    # Do crossover in sorted lists
    if self.cType == 0:
        return singlepc(lists[0], lists[1])
    # elif self.cType == 1:


def splitter(self, codeStr):
    # split the code into a list of strings by line