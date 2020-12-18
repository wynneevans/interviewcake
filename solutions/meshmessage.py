"""
BFS(graph, start_node, end_node):
    frontier = new Queue()
    frontier.enqueue(start_node)
    explored = new Set()

    while frontier is not empty:
        current_node = frontier.dequeue()
        if current_node in explored: continue
        if current_node == end_node: return success

        for neighbor in graph.get_neighbours(current_node):
            frontier.enqueue(neighbor)
        explored.add(current_node)
"""


def bfs(graph, start, end):
    visited, queue = [], [start]
    how_we_reached_nodes = {start: None}
    while queue:
        node = queue.pop(0)
        visited.append(node)
        if node == end:
            return how_we_reached_nodes

        for neighbour in graph[node]:
            if neighbour not in visited:
                queue.append(neighbour)
                how_we_reached_nodes[neighbour] = node

    return None


def dfs(graph, start, end):
    visited, stack = list(), [start]
    while stack:
        vertex = stack.pop()

        if vertex not in visited:
            visited.append(vertex)
            for neighbour in graph[vertex]:
                stack.append(neighbour)

        if vertex == end:
            return visited
    return None


def get_path(graph, start_node, end_node):
    if start_node not in graph:
        raise Exception('Start node not in graph')
    if end_node not in graph:
        raise Exception('End node not in graph')

    # Find the shortest route in the network between the two users

    record = bfs(graph, start_node, end_node)

    if not record:
        return None

    print(record)
    path = []
    node = end_node

    while node:
        path.append(node)
        node = record[node]

    path.reverse()

    return path
