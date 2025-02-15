# search.py
# ---------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# For more info, see http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html

"""
In search.py, you will implement generic search algorithms which are called
by Pacman agents (in searchAgents.py).
"""

import util
from util import heappush, heappop
class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
      """
      Returns the start state for the search problem
      """
      util.raiseNotDefined()

    def isGoalState(self, state):
      """
      state: Search state

      Returns True if and only if the state is a valid goal state
      """
      util.raiseNotDefined()

    def getSuccessors(self, state):
      """
      state: Search state

      For a given state, this should return a list of triples,
      (successor, action, stepCost), where 'successor' is a
      successor to the current state, 'action' is the action
      required to get there, and 'stepCost' is the incremental
      cost of expanding to that successor
      """
      util.raiseNotDefined()

    def getCostOfActions(self, actions):
      """
      actions: A list of actions to take

      This method returns the total cost of a particular sequence of actions.  The sequence must
      be composed of legal moves
      """
      util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other
    maze, the sequence of moves will be incorrect, so only use this for tinyMaze
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s,s,w,s,w,w,s,w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.
    Your search algorithm needs to return a list of actions that reaches
    the goal. Make sure that you implement the graph search version of DFS,
    which avoids expanding any already visited states. 
    Otherwise your implementation may run infinitely!
    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:
    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    """
    YOUR CODE HERE
    """
    
    #in the form (34,16)
    startState= problem.getStartState()
    
    #check if start state is goal and return empty directions if so
    if problem.isGoalState(startState):
      return []
    
    #queue (stack) used for DFS and array of visited nodes, initialized to empty
    q= util.Stack()
    visited=[]
    q.push((startState,[]))
    
    while not q.isEmpty():
      #get next node
      curr, actions= q.pop()
      
      #if current node is the goal state, return list of actions to get there
      if problem.isGoalState(curr):
        print(actions)
        return actions
        
      if curr not in visited:
        #if current node has not been visited yet, "expand" it
        #add curr to visited list
        visited.append(curr)
        
        #if its not the goal state
        for next, action, cost in problem.getSuccessors(curr): 
          #add action to get to successor to actions list and push onto queue to explore
          q.push((next, actions[:] + [action]))

  
  
    util.raiseNotDefined()
    

def breadthFirstSearch(problem):
    """
    YOUR CODE HERE
    """
    
    #in the form (34,16)
    startState= problem.getStartState()
    
    #check if start state is goal and return empty directions if so
    if problem.isGoalState(startState):
      return []
    
    #queue used for BFS and array of visited nodes, initialized to empty
    q= util.Queue()
    visited=[]
    q.push((startState,[]))
    
    while not q.isEmpty():
      #get next node
      curr, actions= q.pop()
      
      #if current node is the goal state, return list of actions to get there
      if problem.isGoalState(curr):
        print(actions)
        return actions
        
      if curr not in visited:
        #if current node has not been visited yet, "expand" it
        #add curr to visited list
        visited.append(curr)
        
        #if its not the goal state
        for next, action, cost in problem.getSuccessors(curr): 
          #add action to get to successor to actions list and push onto queue to explore
          q.push((next, actions[:] + [action]))
  
    util.raiseNotDefined()

def uniformCostSearch(problem):
    """
    YOUR CODE HERE
    """
    
    #in the form (34,16)
    startState= problem.getStartState()
    
    #check if start state is goal and return empty directions if so
    if problem.isGoalState(startState):
      return []
    
    #queue used for UCS is a priorityQueue and array of visited nodes, initialized to empty
    q= util.PriorityQueue()
    visited=[]
    #((node , actions to current node , total cost to current node),priority)
    q.push((startState,[],0),0)
    
    while not q.isEmpty():
      #get next node
      curr, actions, cost= q.pop()
      
      #if current node has not been visited yet, "expand" it
      if curr not in visited:
        
        #add curr to visited list
        visited.append(curr)
        
        #if current node is the goal state, return list of actions to get there
        if problem.isGoalState(curr):
          return actions
        
        #if its not the goal state
        for next, action, nextCost in problem.getSuccessors(curr):
          #add action to get to successor to actions list and push onto queue to explore
          q.push((next, actions + [action], cost+nextCost),cost+nextCost)
    
  
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """
    YOUR CODE HERE
    """
    
    #in the form (34,16)
    startState= problem.getStartState()
    
    #check if start state is goal and return empty directions if so
    if problem.isGoalState(startState):
      return []
    
    #queue used for aStar is a priorityQueue and array of visited nodes, initialized to empty
    q= util.PriorityQueue()
    visited=[]
    #((node , actions to current node , total cost to current node),priority)
    q.push((startState,[],0),0)
    
    while not q.isEmpty():
      #get next node
      curr, actions, cost= q.pop()
      
      #if current node has not been visited yet, "expand" it
      if curr not in visited:
        
        #add curr to visited list
        visited.append(curr)
        
        #if current node is the goal state, return list of actions to get there
        if problem.isGoalState(curr):
          return actions
        
        #if its not the goal state
        for next, action, nextCost in problem.getSuccessors(curr):
          #add action to get to successor to actions list and push onto queue to explore
          heuristicCost= cost+ nextCost + heuristic(next,problem)
          q.push((next, actions + [action], cost+nextCost), heuristicCost)
    
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch


    
