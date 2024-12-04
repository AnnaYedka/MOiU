from collections import defaultdict


def ford_fulkerson(graph, s, t):
    # step 1
    f = defaultdict(lambda: defaultdict(int))

    # step 2
    G_f = defaultdict(dict)
    for u in graph:
        for v, c in graph[u].items():
            G_f[u][v] = c - f[u][v] + f[v][u]

    # step 3
    while True:
        path = bfs_find_path(G_f, s, t)
        if t not in path:
            return f

        # step 4
        v = t
        P = []
        while v != s:
            P.append(v)
            v = path[v]
        P.append(s)
        P = P[::-1]

        theta = min([G_f[P[i]][P[i+1]] for i in range(len(P) - 1)])

        f_p = defaultdict(lambda: defaultdict(int))

        for i in range(len(P)-1):
            f_p[P[i]][P[i+1]] = theta

        f_new = defaultdict(lambda: defaultdict(int))
        for u in G_f.keys():
            for v in G_f[u].keys():
                f_new[u][v] = max(0, f[u][v] - f[v][u] + f_p[u][v] - f_p[v][u])
        f = f_new

        for i in range(len(P)-1):
            G_f[P[i]][P[i+1]] -= theta
            G_f[P[i+1]][P[i]] += theta


def bfs_find_path(G_f, s, t):
    Q = [s]
    l = {s: None}
    while Q and t not in l:
        v = Q.pop(0)
        for u, c in G_f[v].items():
            if u not in l and c > 0:
                l[u] = v
                Q.append(u)
    return l

def defaultdict_to_dict(d):
    if isinstance(d, defaultdict):
        return {key: defaultdict_to_dict(value) for key, value in d.items()}
    else:
        return d

if __name__ == '__main__':
    G = {
        's': {'a': 3, 'b': 2},
        'a': {'s': 0, 'b': 2, 't': 1},
        'b': {'s': 0, 'a': 0, 't': 2},
        't': {'a': 0, 'b': 0}
    }

    res = ford_fulkerson(G, 's', 't')
    print(defaultdict_to_dict(res))