def dfs(graph: dict, s: str, t: str, path=None):
    if not path:
        path = []

    path.append(s)
    if s == t:
        return path

    for neighbor in graph.get(s):
        if neighbor not in path:
            new_path = dfs(graph, neighbor, t, path.copy())
            if new_path:
                return new_path

    return None

def add_to_graph(graph: dict, u: str, v: str):
    if not graph.get(u):
        graph[u] = [v]
    else:
        graph[u].append(v)


def find_max_matching(G, V_1, V_2):
    graph = {}

    # step 1
    for u, v in G:
        if u in V_1:
            add_to_graph(graph, u, v)
        else:
            add_to_graph(graph, v, u)

    # step 2
    graph.update({'s': V_1.copy()})
    for v in V_2:
        add_to_graph(graph, v, 't')

    while True:
        # step 3
        path = dfs(graph, 's', 't')

        # step 4
        if not path:
            M = []
            for u in V_2:
                for v in graph.get(u):
                    if v in V_1:
                        M.append((v, u))
            return M

        # step 5
        graph[path[0]].remove(path[1])
        graph[path[-2]].remove(path[-1])

        for i in range(1, len(path) - 2):
            graph[path[i]].remove(path[i + 1])
            add_to_graph(graph, path[i+1], path[i])



if __name__ == '__main__':
    V_1 = ['a', 'b', 'c']
    V_2 = ['x', 'y', 'z']
    G = [('a', 'x'), ('b', 'x'), ('b', 'y'), ('c', 'x'), ('c', 'y'), ('c', 'z')]
    print(find_max_matching(G, V_1, V_2))