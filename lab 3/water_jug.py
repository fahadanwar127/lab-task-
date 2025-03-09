from collections import deque


def is_goal_state(state, goal):
    return goal in state


def get_neighbors(state, X, Y):
    A, B = state
    neighbors = []

    neighbors.append((X, B))
    
    
    neighbors.append((A, Y))
    
    
    neighbors.append((0, B))
    
    
    neighbors.append((A, 0))
    
    
    transfer = min(A, Y - B)
    neighbors.append((A - transfer, B + transfer))
    

    transfer = min(B, X - A)
    neighbors.append((A + transfer, B - transfer))
    
    return neighbors


def dfs(X, Y, goal):

    start = (0, 0)
    
    
    stack = [start]

    visited = set()
    visited.add(start)
    
    while stack:
        state = stack.pop()
        
        # If goal is reached, print the state
        if is_goal_state(state, goal):
            print(f"Goal reached with state: {state}")
            return True
        
        # Get possible neighbors (new states)
        for neighbor in get_neighbors(state, X, Y):
            if neighbor not in visited:
                visited.add(neighbor)
                stack.append(neighbor)
    
    print("Goal not reachable.")
    return False

X = 4 
Y = 3  
goal = 2  
dfs(X, Y, goal)
