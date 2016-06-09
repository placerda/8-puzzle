# -*- coding: iso-8859-1 -*-
import search
import random
import pdb

# enviar para adriana@addlabs.uff.br

# Module Classes

class EightPuzzleState:
 """
 The Eight Puzzle is described in the course textbook on
 page 64.

 This class defines the mechanics of the puzzle itself.  The
 task of recasting this puzzle as a search problem is left to
 the EightPuzzleSearchProblem class.
 """

 def __init__( self, numbers ):
  self.cells = []
  numbers = numbers[:] # Make a copy so as not to cause side-effects.
  numbers.reverse()
  for row in range( 3 ):
    self.cells.append( [] )
    for col in range( 3 ):
        self.cells[row].append( numbers.pop() )
        if self.cells[row][col] == 0:
          self.blankLocation = row, col
  self.parent = None
  self.cost   = 0
  self.move   = 'initial'
  self.goal = [[1,2,3], [8,0,4], [7,6,5]]

 def isGoal( self ):
   """
     Checks to see if the puzzle is in its goal state.

       -------------
       |   | 1 | 2 |
       -------------
       | 3 | 4 | 5 |
       -------------
       | 6 | 7 | 8 |
       -------------

   >>> EightPuzzleState([1, 2, 3, 8, 0, 4, 7, 6, 5]).isGoal()
   True

   >>> EightPuzzleState([1, 0, 2, 3, 4, 5, 6, 7, 8]).isGoal()
   False
   """
   current = self.goal
   for row in range( 3 ):
    for col in range( 3 ):
      if current[row][col] != self.cells[row][col]:
        return False
   return True

 def legalMoves( self ):
   """
     Returns a list of legal moves from the current state.

   Moves consist of moving the blank space up, down, left or right.
   These are encoded as 'up', 'down', 'left' and 'right' respectively.

   >>> EightPuzzleState([0, 1, 2, 3, 4, 5, 6, 7, 8]).legalMoves()
   ['down', 'right']
   """
   moves = []
   row, col = self.blankLocation
   if(row != 0):
     moves.append('up')
   if(row != 2):
     moves.append('down')
   if(col != 0):
     moves.append('left')
   if(col != 2):
     moves.append('right')
   return moves

 def result(self, move):
   """
     Returns a new eightPuzzle with the current state and blankLocation
   updated based on the provided move.

   The move should be a string drawn from a list returned by legalMoves.
   Illegal moves will raise an exception, which may be an array bounds
   exception.

   NOTE: This function *does not* change the current object.  Instead,
   it returns a new object.
   """
   row, col = self.blankLocation
   if(move == 'up'):
     newrow = row - 1
     newcol = col
   elif(move == 'down'):
     newrow = row + 1
     newcol = col
   elif(move == 'left'):
     newrow = row
     newcol = col - 1
   elif(move == 'right'):
     newrow = row
     newcol = col + 1
   else:
     raise "Illegal Move"

   # Create a copy of the current eightPuzzle
   newPuzzle = EightPuzzleState([0, 0, 0, 0, 0, 0, 0, 0, 0])
   newPuzzle.cells = [values[:] for values in self.cells]
   # And update it to reflect the move
   newPuzzle.cells[row][col] = self.cells[newrow][newcol]
   newPuzzle.cells[newrow][newcol] = self.cells[row][col]
   newPuzzle.blankLocation = newrow, newcol
   newPuzzle.parent = self
   newPuzzle.move = move
   return newPuzzle

 # Utilities for comparison and display
 def __eq__(self, other):
   """
       Overloads '==' such that two eightPuzzles with the same configuration
     are equal.

     >>> EightPuzzleState([0, 1, 2, 3, 4, 5, 6, 7, 8]) == \
         EightPuzzleState([1, 0, 2, 3, 4, 5, 6, 7, 8]).result('left')
     True
   """
   for row in range( 3 ):
      if self.cells[row] != other.cells[row]:
        return False
   return True

 def __hash__(self):
   return hash(str(self.cells))

 def __getAsciiString(self):
   """
     Returns a display string for the puzzle
   """
   lines = []
   horizontalLine = ('-' * (13))
   lines.append(horizontalLine)
   for row in self.cells:
     rowLine = '|'
     for col in row:
       if col == 0:
         col = ' '
       rowLine = rowLine + ' ' + col.__str__() + ' |'
     lines.append(rowLine)
     lines.append(horizontalLine)
   return '\n'.join(lines)

 def __str__(self):
   return self.__getAsciiString()

# TODO: Implement The methods in this class

class EightPuzzleSearchProblem(search.SearchProblem):
  """
      Implementation of a SearchProblem for the  Eight Puzzle domain

    Each state is represented by an instance of an eightPuzzle.
  """
  def __init__(self,puzzle):
    """
       Creates a new EightPuzzleSearchProblem which stores search information.
    """
    self.puzzle = puzzle
    self.numNodesExpanded = 0
    self.expandedNodeSet = {}

  def getStartState(self):
    """
        Returns the initial state
    """
    # Your code here
    return self.puzzle
      
  def isGoalState(self,state):
    """
        Returns true if the state is a goal state
    """
    # Your code here
    return state.isGoal()
   
  def getSuccessors(self,state):
    """
      state: an eight puzzle

    Returns list of (successor,cost) pairs where
    each succesor is either left, right, up, or down
    from the original state and the cost is 1.0 for each
    """
    # Leave these lines in.  They keep track of the search progress
    self.numNodesExpanded += 1
    self.expandedNodeSet[state] = 1

    # Your code here
    sucessors = []
    legalMoves = state.legalMoves()
    for move in legalMoves:
      sucessors.append(state.result(move))
    return sucessors

  # Search Stats

  def displaySearchStats(self):
    """
      Display number of nodes expanded by 'getSuccessors'
    """
    print 'Number of nodes expanded:',self.numNodesExpanded
    print 'Number of unique nodes expanded:', len(self.expandedNodeSet)

  def resetSearchStats(self):
    self.numNodesExpanded = 0
    self.expandedNodeSet = {}

# Heuristics

def misplacedTiles(state, eightPuzzleSearchProblem):
  """
    state: An eight puzzle
    eightPuzzleSearchProblem: Eight puzzle search problem

    Returns the number of misplaced tiles.
  """
  # Your code here
  #pdb.set_trace()
  cost = 0
  goal = eightPuzzleSearchProblem.getStartState().goal
  for i in range(0,3):
      for j in range(0,3):
        #pdb.set_trace()
        if (state.cells[i][j] != goal[i][j]):
            cost += 1
  state.cost = cost
  return cost

def manhattanDistance(state, eightPuzzleSearchProblem):
  """
    state: An eight puzzle

    Returns the sume of the distances between each
    tile's current location and its proper place.
  """
  # Your code here
  cost = 0
  goal = eightPuzzleSearchProblem.getStartState().goal
  for i in range(0,3):
      for j in range(0,3):
        current = state.cells[i][j]
        for k in range(0,3):
          for l in range(0,3):
            if current == goal[k][l]:
              cost += abs(k-i) + abs(l-j)
  state.cost = cost
  return cost

# Module Methods

EIGHT_PUZZLE_DATA = [[1, 2, 3, 8, 4, 0, 7, 6, 5], 
                     [1, 2, 3, 8, 4, 5, 7, 0, 6], 
                     [1, 2, 3, 8, 4, 5, 0, 7, 6], 
                     [5, 4, 3, 6, 1, 8, 7, 0, 2]]

def loadEightPuzzle(puzzleNumber):
  """
    puzzleNumber: The number of the eight puzzle to load.
    
    Returns an eight puzzle object generated from one of the
    provided puzzles in EIGHT_PUZZLE_DATA.
    
    puzzleNumber can range from 0 to 5.
    
    >>> print loadEightPuzzle(0)
    -------------
    | 1 |   | 2 |
    -------------
    | 3 | 4 | 5 |
    -------------
    | 6 | 7 | 8 |
    -------------
  """
  return EightPuzzleState(EIGHT_PUZZLE_DATA[puzzleNumber])

def createRandomEightPuzzle(moves=100):
 """
   moves: number of random moves to apply

   Creates a random eight puzzle by applying
   a series of 'moves' random moves to a solved
   puzzle.
 """
 puzzle = EightPuzzleState([0,1,2,3,4,5,6,7,8])
 for i in range(moves):
   # Execute a random legal move
   puzzle = puzzle.result(random.sample(puzzle.legalMoves(), 1)[0])
 return puzzle