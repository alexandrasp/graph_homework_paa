#!/usr/bin/python

import sys
import numpy as npy
from graph import Graph
from voluntary import Voluntary
import timeit

sys.argv[1:]

myGraph = Graph()
volu = Voluntary()

fileInput = open(sys.argv[1], 'r')
fileOutput = open(sys.argv[2], 'w')

finalSet = []

V, E = fileInput.readline().strip().split(' ')

for x in range(int(V)):
    volu = Voluntary()
    volu.nodeId = x
    myGraph.addVertices(volu)

for x in range(int(E)):
    v1, v2 = fileInput.readline().strip().split(' ')
    myGraph.addEdge(v1, v2)

F = fileInput.readline().strip()

for x in range(0, int(V)):
    a = fileInput.readline().strip().split(' ')
    if len(a)>1:
        for y in range(0, len(a)):
            volu.addFocus(myGraph.vertices[x], a[y])
    else:
        volu.addFocus(myGraph.vertices[x], a[0])

fileInput.close()

start_time = timeit.default_timer()
finalSet = myGraph.coberturaFocos(V, F)
for x in range (0, len(finalSet)):
    fileOutput.write(str(int(finalSet[x].nodeId+1))+" ")
print(timeit.default_timer() - start_time, " seconds")
fileOutput.close()

