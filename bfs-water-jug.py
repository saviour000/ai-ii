from collections import deque

def is_valid(state, visited):
    return state not in visited

def bfs_water_jug(jug1_capacity, jug2_capacity, target):
    visited = set()
    parent = {}
    queue = deque()

    start = (0, 0)
    queue.append(start)
    visited.add(start)
    parent[start] = None

    while queue:
        x, y = queue.popleft()

        if x == target or y == target:
            path = []
            current = (x, y)
            while current is not None:
                path.append(current)
                current = parent[current]
            path.reverse()
            return path

        next_states = [
            (jug1_capacity, y),
            (x, jug2_capacity),
            (0, y),
            (x, 0),
            (0, x + y) if x + y <= jug2_capacity else (x - (jug2_capacity - y), jug2_capacity),
            (x + y, 0) if x + y <= jug1_capacity else (jug1_capacity, y - (jug1_capacity - x))
        ]

        for state in next_states:
            if is_valid(state, visited):
                visited.add(state)
                parent[state] = (x, y)
                queue.append(state)

    return None

jug1 = 4
jug2 = 3
target = 2
solution_path = bfs_water_jug(jug1, jug2, target)

if solution_path:
    print("Solution steps:")
    for step in solution_path:
        print(step)
else:
    print("No solution found.")