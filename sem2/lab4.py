def backpack_task(v, c, B):
    n = len(v)
    opt = [[0] * (B + 1) for _ in range(n + 1)]

    for i in range(1, n+1):
        for j in range(B+1):
            if v[i-1] <= j:
                opt[i][j] = max(opt[i-1][j], opt[i-1][j-v[i-1]] + c[i-1])
            else:
                opt[i][j] = opt[i-1][j]

    max_cost = opt[n][B]
    items = []
    weight_left = B
    for i in range(n, 0, -1):
        if opt[i][weight_left] != opt[i-1][weight_left]:
            items.append(i-1)
            weight_left -= v[i-1]
    return max_cost, items


if __name__ == '__main__':
    v = (6, 4, 3, 2, 5)
    c = (5, 3, 1, 3, 6)
    B = 15
    print(backpack_task(v, c, B))
