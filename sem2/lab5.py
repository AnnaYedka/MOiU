def topological_sort(graph):
    visited = set()
    stack = []

    def dfs(node):
        if node in visited:
            return
        visited.add(node)
        for child in graph[node]:
            if child not in visited:
                dfs(child)
        stack.append(node)

    for node in graph:
        if node not in visited:
            dfs(node)

    return stack[::-1]


def longest_path_to_target(graph, s, t):
    sorted_nodes = topological_sort(graph)

    opt = {node: float('-inf') for node in graph}
    x = {node: '' for node in graph}
    opt[s] = 0

    for node in sorted_nodes:
        if opt[node] != float('-inf'):
            for child, weight in graph[node].items():
                if opt[child] < opt[node] + weight:
                    opt[child] = opt[node] + weight
                    x[child] = node
            if node == t:
                return opt[t], ' '.join(x[node] for node in sorted_nodes)

    return "Путь недостижим"


if __name__ == '__main__':
    graph = {
        's': {'a':3, 'c':2},
        'a': {'b':4},
        'b': {'t':2, 'd':2},
        'c': {'a': 2, 'd': 2},
        'd': {'t':1},
        't': {}
    }

    print(longest_path_to_target(graph, 's', 't'))
