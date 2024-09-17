import numpy as np
from .lab1 import inverse_matrix


def dual_simplex_method(c, A, b, B):
	# step 1
	AB_inv = np.linalg.inv(A[:, B])

	while True:

		# step 2
		cB = c[B]

		# step 3
		y = cB @ AB_inv

		# step 4
		n = len(A[0])
		kB = AB_inv @ b

		k = np.zeros(n)
		for i in range(len(B)):
			k[B[i]] = kB[i]

		# step 5
		if np.all(k >= 0):
			return k

		# step 6
		jk = np.where(k < 0)[0][0]
		k_indx = np.where(B == jk)[0][0]

		# step 7
		delta_y = AB_inv[k_indx]
		mu = np.zeros(n)
		indexes = np.setdiff1d(np.arange(n), B)
		for j in indexes:
			mu[j] = delta_y @ A[:, j]

		# step 8
		if np.all(mu >= 0):
			raise Exception('задача несовместна')

		sigma = np.full(n, np.inf)
		for j in indexes:
			if mu[j] < 0:
				sigma[j] = (c[j] - A[:, j] @ y) / mu[j]

		j_0 = np.argmin(sigma)
		B[k_indx] = j_0

		replace_column = A[:, j_0]
		AB_inv = inverse_matrix(AB_inv, replace_column, len(replace_column), k_indx)


if __name__ == "__main__":
	c = np.array([-4, -3, -7, 0, 0])
	A = np.array([
		[-2, -1, -4, 1, 0],
		[-2, -2, -2, 0, 1],
	])
	b = np.array([-1, -1.5])
	B = np.array([3, 4])

	x = dual_simplex_method(c, A, b, B)
	print(x)
