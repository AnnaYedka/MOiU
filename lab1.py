import numpy as np

n = 3
i = 2

A = np.random.randint(0, 20, size=(n, n))
x = np.random.randint(0, 20, size=(n,))

inv_A = np.linalg.inv(A)
l = inv_A @ x

if not l[i]:
	print("replaced matrix is not inversable")
	raise Exception

l_wave = l.copy()
l_wave[i] = -1
l_top = l_wave / -l[i]
Q = np.eye(n)
Q[:, i] = l_top


res_inv = np.empty((n, n))

for j in range(n):
	for k in range(n):
		if j == i:
			res_inv[j][k] = Q[j][j] * inv_A[j][k]
		else:
			res_inv[j][k] = Q[j][i] * inv_A[i][k] + Q[j][j] * inv_A[j][k]

print(Q @ inv_A)

print(res_inv)
