import numpy as np

def inverse_matrix(A, x, n, i):

	if not n or i >=n:
		raise Exception('invalid arguments')


	#inv_A = np.linalg.inv(A)
	inv_A = A

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

	return res_inv


if __name__ == '__main__':
	pass