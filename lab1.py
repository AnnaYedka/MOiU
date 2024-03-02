import numpy as np

def inverse_matrix(n, i):
	if not n or i >=n:
		raise Exception('invalid arguments')

	A = np.random.randint(0, 20, size=(n, n))
	x = np.random.randint(0, 20, size=(n,))

	print("A = \n", A)
	print("x = \n", x)


	inv_A = np.linalg.inv(A)

	l = inv_A @ x

	if not l[i]:
		print("replaced matrix is not inversable")
		return

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

	print("inversed matrix O(n3): \n", Q @ inv_A)

	print("inversed matrix O(n2): \n", res_inv)


inverse_matrix(3, 1)
