
def shortest_path(source, target):

    num_explored = 0

        # Initialize frontier to just the starting position
    start = Node(state=source, parent=None, action=None)
    frontier = StackFrontier()
    frontier.add(start)

        # Initialize an empty explored set
    explored = set()

        # Keep looping until solution found
    while True:

            # If nothing left in frontier, then no path
            if frontier.empty():
                raise Exception("no solution")

            # Choose a node from the frontier
            node = frontier.remove()
            num_explored += 1

            # If node is the goal, then we have a solution
            if node.state == target:
                actions = []
                cells = []
                while node.parent is not None:
                    actions.append(node.action)
                    cells.append(node.state)
                    node = node.parent
                actions.reverse()
                cells.reverse()
                solution = (actions, cells)
                return solution

            # Mark node as explored
            explored.add(node.state)

            # Add neighbors to frontier
            for action, state in neighbors_for_person(node.state):
                if not frontier.contains_state(state) and state not in explored:
                    child = Node(state=state, parent=node, action=action)
                    frontier.add(child)
