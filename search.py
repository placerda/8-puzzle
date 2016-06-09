# -*- coding: iso-8859-1 -*-
import util, pdb
## Abstract Search Classes

class SearchProblem:
  """
  Abstract SearchProblem class. Your classes
  should inherit from this class and override 
  all the methods below
  """
  def getStartState(self):
     """
     Returns the start state for the search problem 
     """
     abstract    
        
  def getSuccessors(self, state):
     """
       state: Search state
     
     For a given state should return a list of pairs, (successor,stepCost), 
     where 'successor' is a successor to the current state and
     'stepCost' is the incremental cost of expanding to that successor
     """
     abstract
            
  def isGoalState(self, state):
    """
      state: Search state
    
    Returns True if and only if the state is a valid goal state
    """
    abstract

  # These methods are used to evaluate SearchAgents
  
  def displaySearchStats(self):
    """
      Should display statistics regarding the amount of work
      down during search. For instance, the number of nodes 
      expanded (how many times getSuccessors is called) and
      how many are discovered (found as a successor)
    """
    abstract
  
  def resetSearchStats(self):
    """
      Reset internal state of problem for tracking
      search statistics. All search agents should 
      call this method before doing any searching
    """  
    abstract
   
class SearchAgent:
  """
  Abstract SearchAgent class. Your agents should
  inherit from this class and override the solve
  method. 
  """
  def solve(self, searchProblem):
    """
      searchProblem: SearchProblem subclass
    
    For the passed in 'searchProblem' should return a (solutionPath,cost) pair where
    'solutionPath' is a list of search states representing
    the solution to the problem and 'cost' is total cost of the solution.   
    
    All subclasses should also first call searchProblem.resetSearchStats()
    before doing any searching.
    """
    abstract

## Specific Search Agents
# ***Implement the classes below***
  
class DepthFirstSearchAgent(SearchAgent):
  """
    DepthFirstSearchAgent
    
  Implements depth-first graph search for a given problem.  
  """
  def solve(self,searchProblem):
    """
        searchProblem: Search problem
    
    Solves the given problem using depth first
    search and returns a (solutionPath, cost) where
    'solutionPath' is a valid list of states beggining
    with the start state and ending with a goal state.
    The 'cost' is the cost of the 'solutionPath'.
    """
    return (None,0.0)    
      
class BreadthFirstSearchAgent(SearchAgent):
  """
     Breadth First Search
     
   Implements basic breadth-first-search for a given problem
  """
  def solve(self, searchProblem):
    """
        Solves the given searchProblem using Breadth
    first search.
    
    Returns (solutionPath,cost) pair where
    solutionPath is a list of the states
    starting from the start state to a goal
    state and cost is the total cost of the 
    solution.
    """      
    solutionPath = []
    totalCost = 0

    nodeInitial = searchProblem.getStartState()
    if (searchProblem.isGoalState(nodeInitial)):
      solutionPath.append(nodeInitial)
      totalCost = nodeInitial.cost
      return (solutionPath, totalCost)
   
    frontier = [nodeInitial]
    explored = {}
    searching = True
    nodeSolution = None
    while searching:
      #pdb.set_trace()
      if not frontier: 
        searching = False
      else:
        node = frontier.pop(0)
        explored[node] = 1
        for child in searchProblem.getSuccessors(node):
          child.cost = 1
          #pdb.set_trace()
          #print child[0]        
          if (child not in frontier) and (child not in explored):
            if (searchProblem.isGoalState(child)):
              nodeSolution = child
              solutionPath.append(nodeSolution)
              totalCost += child.cost           
              searching = False
            frontier.append(child)

    if nodeSolution:
      parent = nodeSolution.parent
      while parent:
        #pdb.set_trace()
        if parent:
          solutionPath.insert(0,parent)
          totalCost += parent.cost
        parent = parent.parent

    return solutionPath, totalCost

 
class UniformCostSearchAgent(SearchAgent):
  """
      UniformCostSearchAgent
      
  Implements uniform cost search
  """
  def solve(self, searchProblem):
    """
        searchProblem: Search problem
    
     Solves the given searchProblem using
    uniform cost search.
    
    Returns (solutionPath,cost) pair where
    solutionPath is a list of the states
    starting from the start state to a goal
    state and cost is the total cost of the 
    solution.
    """
    return None, 0.0

class AStarSearchAgent(SearchAgent):
  """
     AStarSearchAgent
     
  Implements A* search. Should take
  a heuristicFn at construction. That
  heuristic function should take a
  state and search problem as its 
  arguments.
  """   
  def __init__(self, heuristicFn):
    self.heuristicFn = heuristicFn 
        
  def solve(self, searchProblem):
    """
      searchProblem: Search Problem
    
    Solves the given searchProblem using AStar
    search with the heuristic function passed
    to the constructor. 
    
    Returns (solutionPath,cost) pair where
    solutionPath is a list of the states
    starting from the start state to a goal
    state and cost is the total cost of the 
    solution.
    
    The solution returned is guranteed to be 
    the minimal cost solution
    """
    solutionPath = []
    totalCost = 0

    #pdb.set_trace()

    nodeInitial = searchProblem.getStartState()
    frontier = util.PriorityQueue()
    frontier.setPriority(nodeInitial, self.heuristicFn(nodeInitial, searchProblem))
    explored = {}
    searching = True
    nodeSolution = None 
    while searching:
      #pdb.set_trace()
      if frontier.isEmpty():
        solutionPath.append(nodeInitial)
        totalCost = nodeInitial.cost
        return (solutionPath, totalCost)
      else:
        node = frontier.dequeue()
        explored[node] = 1
        if (searchProblem.isGoalState(node)):
          nodeSolution = node
          solutionPath.append(nodeSolution)
          totalCost += node.cost           
          searching = False
        else:
          for child in searchProblem.getSuccessors(node):
            if (child not in explored):
              frontier.setPriority(child, self.heuristicFn(child, searchProblem))
    if nodeSolution:
      parent = nodeSolution.parent
      while parent:
        #pdb.set_trace()
        if parent:
          solutionPath.insert(0,parent)
          totalCost += parent.cost
        parent = parent.parent

    return solutionPath, totalCost