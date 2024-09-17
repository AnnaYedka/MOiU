import numpy as np

import lab1


def simplex_method(A, c, b, x, B):
	# step 1
	AB = A[:, B]
	AB_inv = np.linalg.inv(AB)

	while True:

		# step 2
		cB = c[B]

		# step 3
		u = cB @ AB_inv

		# step 4
		delta = u @ A - c

		# step 5
		if np.all(delta >= 0):
			# print('x = ', x)
			# print('B = ', B)
			return x, B

		# step 6
		j0 = np.where(delta < 0)[0][0]

		# step 7
		z = AB_inv @ A[:, j0]

		# step 8
		m = len(B)
		theta = np.array([x[B[i]] / z[i] if z[i] > 0 else np.inf for i in range(m)])

		# step 9
		theta0 = min(theta)

		# step 10
		if theta0 == np.inf:
			print('целевой функционал задачи не ограничен сверху на множестве допустимых планов')
			return

		# step 11
		k = np.where(theta == theta0)[0][0]
		j_star = B[k]

		# step 12
		B[k] = j0

		# step 13
		for i in range(m):
			if i != k:
				x[B[i]] -= theta0 * z[i]
		x[j_star] = 0
		x[j0] = theta0

		replace_column = A[:, j0]
		AB_inv = lab1.inverse_matrix(AB_inv, replace_column, len(replace_column), k)


if __name__ == '__main__':
	c = np.array([1, 1, 0, 0, 0])

	A = np.array([
		[-1, 1, 1, 0, 0],
		[1, 0, 0, 1, 0],
		[0, 1, 0, 0, 1]
	])

	b = np.array([1, 3, 2])
	x = np.array([0, 0, 1, 3, 2])
	B = np.array([2, 3, 4])  # indexing starts at zero, so decremented one

	simplex_method(A, c, b, x, B)
