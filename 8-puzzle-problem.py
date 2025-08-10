from copy import deepcopy

goal_state = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]

moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def find_zero(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

def is_goal(state):
    return state == goal_state

def get_neighbors(state):
    x, y = find_zero(state)
    neighbors = []
    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = deepcopy(state)
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            neighbors.append(new_state)
    return neighbors

def dfs(start_state, max_depth=50):
    stack = [(start_state, [start_state])]
    visited = set()

    while stack:
        state, path = stack.pop()
        state_tuple = tuple(map(tuple, state))

        if state_tuple in visited:
            continue
        visited.add(state_tuple)

        if is_goal(state):
            return path

        if len(path) <= max_depth:
            for neighbor in get_neighbors(state):
                stack.append((neighbor, path + [neighbor]))

    return None

initial_state = [
    [1, 2, 3],
    [4, 0, 6],
    [7, 5, 8]
]

solution = dfs(initial_state)

if solution:
    print(f"Solution found in {len(solution)-1} moves using DFS:")
    for step in solution:
        for row in step:
            print(row)
        print()
else:
    print("No solution found (may be due to depth limit).")