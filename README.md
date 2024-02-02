# 8-Puzzle
This Python script demonstrates a solution to the classic 8-puzzle problem using the A* search algorithm with the Manhattan distance heuristic. The code includes a PuzzleNode class representing states in the puzzle search space, and the a_star function performs the search to find the optimal solution path.

PuzzleNode Class
- Represents a node in the puzzle search space with state, parent, action, and depth attributes.
- Implements comparison, equality, and hash functions for use in A* search.
- Checks if the node's state matches the goal state and finds the position of the blank (0) in the puzzle.
- Generates child nodes by making valid moves from the current state.
- Calculates the Manhattan distance heuristic for the node's state.
A* Search Algorithm
- Utilizes a priority queue (heapq) to explore nodes with lower total costs first.
- The main loop continues until the goal state is reached or no solution is found.
- Explores child nodes, considering their cost and heuristic value, and updates the frontier and explored sets accordingly.
Example Usage
- The script includes an example usage section with a predefined initial state.
- If a solution is found, it prints the solution path with each step, otherwise, it indicates that no solution was found.
