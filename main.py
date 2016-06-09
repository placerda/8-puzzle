#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-
import puzzle 
import search 
import pdb

#Seleciona o puzzle
puzz = puzzle.loadEightPuzzle(3) 
puzzleProblem = puzzle.EightPuzzleSearchProblem(puzz) 

#Seleciona o tipo de busca
#s = search.BreadthFirstSearchAgent() #BFS
#s = search.AStarSearchAgent(puzzle.misplacedTiles) #Heuristic Misplace Tiles
s = search.AStarSearchAgent(puzzle.manhattanDistance) #Heuristic Manhattan Distance

#pdb.set_trace()

#Faz a busca e mostra os resultados
solutionPath, cost =  s.solve(puzzleProblem)
for no in solutionPath:
	print no.move
	print no	
print "cost %d" % cost
puzzleProblem.displaySearchStats()

