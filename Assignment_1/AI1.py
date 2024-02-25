def create_graph():
    graph = {}
    while True:
        vertex = input("Enter a vertex (or type 'done' to finish): ").strip()
        if vertex.lower() == 'done':
            break
        edges = input("Enter edges for vertex {} separated by spaces: ".format(vertex)).strip().split()
        graph[vertex] = edges
    return graph

def print_graph(graph):
    print("Graph:")
    for vertex, edges in graph.items():
        print(f"{vertex}: {', '.join(edges)}")

def bfs(graph, start):
    visited = []
    queue = [start]

    print("Breadth-First Search:")
    while queue:
        node = queue.pop(0)
        if node not in visited:
            print(node, end=' ')
            visited.append(node)
            queue.extend([neighbor for neighbor in graph[node] if neighbor not in visited])

def dfs(graph, start, visited=None):
    if visited is None:
        visited = []

    if start not in visited:
        print(start, end=' ')
        visited.append(start)
        for neighbor in graph[start]:
            dfs(graph, neighbor, visited)

# Take user input to create the graph
print("Create the graph:")
graph = create_graph()

# Print the graph
print_graph(graph)

while True:
    print("\n" + '*' * 10, "MENU", '*' * 10 + "\n")
    print("1. BFS\n2. DFS\n3. Exit\n")

    choice = int(input("Enter your choice: "))
    if choice == 1:
        start_node = input("Enter the starting node for BFS: ")
        bfs(graph, start_node)
    elif choice == 2:
        start_node = input("Enter the starting node for DFS: ")
        print("Depth-First Search:")
        dfs(graph, start_node)
    elif choice == 3:
        break
    else:
        print("Invalid choice. Please enter again.")
