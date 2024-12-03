import numpy as np
from lab6 import find_max_matching

def hungarian_algorithm(C):
    n = C.shape[0]

    # step 1
    alpha = np.zeros((n,), dtype=int)
    beta = np.min(C, axis=0)

    while True:
        # step 2
        J_eq = [(i, j) for i in range(n) for j in range(n) if alpha[i] + beta[j] == C[i][j]]
        # J_lt = [(i, j) for i in range(n) for j in range(n) if alpha[i] + beta[j] < C[i][j]]

        # step 3
        V_1 = ['u' + str(i ) for i in range(n)]
        V_2 = ['v' + str(i) for i in range(n)]
        G = [('u' + str(i), 'v' + str(j)) for i, j in J_eq]

        # step 4
        M, G_star = find_max_matching(G, V_1, V_2)

        # step 5
        if len(M) == n:
            return [(int(u[1:]), int(v[1:])) for u, v in M]

        # step 6, 7
        I = set()
        J = set()

        def populate_i_j(s='s'):
            for u in G_star.get(s):
                i = int(u[1:])
                if u in V_1:
                    I.add(i)
                else:
                    J.add(i)
                populate_i_j(u)

        populate_i_j()

        # step 8
        alpha_new = [1 if i in I else -1 for i in range(n)]
        beta_new = [-1 if i in J else 1 for i in range(n)]

        # step 9
        theta = float('inf')
        for i in I:
            for j in [i for i in range(n) if i not in J]:
                val = (C[i][j] - alpha[i] - beta[j]) / 2
                if val < theta:
                    theta = val

        # step 10
        alpha = [alpha[i] + theta * alpha_new[i] for i in range(n)]
        beta = [beta[i] + theta * beta_new[i] for i in range(n)]

if __name__ == '__main__':
    C = np.array([
        [7, 2, 1, 9, 4],
        [9, 6, 9, 5, 5],
        [3, 8, 3, 1, 8],
        [7, 9, 4, 2, 2],
        [8, 4, 7, 4, 8]
    ])

    print(hungarian_algorithm(C))