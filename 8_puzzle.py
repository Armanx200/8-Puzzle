import heapq

class PuzzleNode:
    def __init__(self, state, parent=None, action=None):
        # Represents a node in the puzzle search space
        self.state = state
        self.parent = parent
        self.action = action
        self.depth = 0
        if parent:
            # Calculate the depth of the node in the search tree
            self.depth = parent.depth + 1

    def __lt__(self, other):
        # Comparison function for priority queue ordering in A* search
        return self.depth + self.manhattan_distance() < other.depth + other.manhattan_distance()

    def __eq__(self, other):
        # Equality check for nodes
        return self.state == other.state

    def __hash__(self):
        # Hash function for storing nodes in sets
        return hash(tuple(map(tuple, self.state)))

    def is_goal(self):
        # Check if the node's state is the goal state
        goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
        return self.state == goal_state

    def get_blank_position(self):
        # Find the position of the blank (0) in the puzzle
        for i, row in enumerate(self.state):
            for j, value in enumerate(row):
                if value == 0:
                    return i, j

    def generate_children(self):
        # Generate child nodes by making valid moves from the current state
        children = []
        i, j = self.get_blank_position()
        possible_moves = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]

        for move in possible_moves:
            if 0 <= move[0] < 3 and 0 <= move[1] < 3:
                # Swap the blank with a neighboring tile
                new_state = [row[:] for row in self.state]
                new_state[i][j], new_state[move[0]][move[1]] = new_state[move[0]][move[1]], new_state[i][j]
                children.append(PuzzleNode(new_state, self, move))

        return children

    def manhattan_distance(self):
        # Calculate the Manhattan distance heuristic for the node's state
        distance = 0
        for i in range(3):
            for j in range(3):
                if self.state[i][j] != 0:
                    value = self.state[i][j] - 1
                    goal_row, goal_col = divmod(value, 3)
                    distance += abs(i - goal_row) + abs(j - goal_col)
        return distance

def a_star(initial_state):
    # A* search algorithm
    initial_node = PuzzleNode(initial_state)
    frontier = [initial_node]
    explored = set()

    while frontier:
        current_node = heapq.heappop(frontier)

        if current_node.is_goal():
            # Return the solution path if the goal state is reached
            return get_solution_path(current_node)

        explored.add(current_node)

        for child in current_node.generate_children():
            if child not in explored and child not in frontier:
                heapq.heappush(frontier, child)

def get_solution_path(node):
    # Retrieve the solution path from the goal node to the initial state
    path = []
    while node:
        path.append(node.state)
        node = node.parent
    return path[::-1]

if __name__ == "__main__":
    # Example initial state
    initial_state = [[1, 2, 3], [4, 5, 6], [0, 7, 8]]
    solution_path = a_star(initial_state)

    if solution_path:
        print("Solution Path:")
        for step, state in enumerate(solution_path):
            print(f"Step {step + 1}:")
            for row in state:
                print(row)
            print("\n")
    else:
        print("No solution found.")