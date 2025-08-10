import itertools


graph = [
    [0,10,15,20],
    [10,0,35,25],
    [15,35,0,30],
    [20,25,30,0],
]

city_names = ['A', 'B' , 'C', 'D']
num_cities = len(graph)

start = 0
cities = list(range(num_cities))

min_cost = float('inf')
best_paths = []

for perm in itertools.permutations(cities[1:]):
    path = [start] + list(perm) + [start]  # complete round-trip
    cost = 0
    for i in range(len(path) - 1):
        cost += graph[path[i]][path[i + 1]]
        
    name_path = [city_names[i] for i in path]
    print(f"Path: {'->'.join(name_path)},Cost:{cost}")
    
    if cost < min_cost:
        min_cost = cost
        best_paths = [path]
    elif cost == min_cost:
        best_paths.append(path)

# Print results
print("\nShortest Path(s):")

for path in best_paths:
    name_path = [city_names[i] for i in path]
    print(f'{'->'.join(name_path)}')