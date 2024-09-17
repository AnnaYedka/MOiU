from typing import List

import numpy as np
from sem1.lab4 import dual_simplex_method


def branch_and_bound_method(c_init, A, b, d_minus, d_plus):
	n, m = len(A[0]), len(A)
	c = np.copy(c_init)
	# step 1
	for i in range(n):
		if c[i] > 0:
			c[i] *= -1
			A[:, i] *= -1
			d_minus[i], d_plus[i] = -d_plus[i], -d_minus[i]

	# step 2
	A_ext = np.concatenate([np.concatenate([A, np.eye(n)], axis=0), np.eye(m + n)], axis=1)
	b_ext = np.concatenate([b, d_plus])
	d_minus = np.pad(d_minus, (0, n + m), 'constant')
	alpha = 0
	c_ext = np.pad(c, (0, n + m), 'constant')

	# step 3
	x_star = None
	r = None
	stack = [(A_ext, b_ext, alpha, c_ext, d_minus, d_minus)]

	# step 4
	while stack:
		A, b, alpha, c, d_minus, delta = stack.pop()
		alpha_1 = alpha + c @ d_minus
		b_1 = b - A @ d_minus
		B = [j for j in range(n, 2 * n + m)]
		x = dual_simplex_method(c, A, b_1, B)
		# case 1
		if array_is_whole(x):
			x = np.add(x, delta)
			if x_star is None or c @ x + alpha_1 > r:
				x_star = x
				r = c @ x + alpha_1
		else:
			# case 2
			if x_star is None or np.floor(c @ x + alpha_1) > r:
				i = 0
				while x[i].is_integer():
					i += 1
				b_2 = np.copy(b_1)
				b_2[m + i] = np.floor(x[i])
				stack.append((A, b_2, alpha_1, c_ext, np.zeros([2 * n + m]), delta))
				d_minus = np.zeros([2 * n + m])
				d_minus[i] = np.ceil(x[i])
				stack.append(
					(A, b_1, alpha_1, c_ext, d_minus, np.add(delta, d_minus)))
	# case 1
	if x_star is None:
		raise Exception('задача несовместна')
	for i in range(n):
		if c_init[i] >= 0:
			x_star[i] *= -1
	return x_star[:n]


def array_is_whole(a: List[float]):
	for val in a:
		if not val.is_integer():
			return False
	return True


if __name__ == "__main__":
	c = np.array([1, 1])
	A = np.asarray([
		[5, 9],
		[9, 5]
	])
	b = np.array([63, 63])
	d_minus = np.array([1, 1])
	d_plus = np.array([6, 6])

	x = branch_and_bound_method(c, A, b, d_minus, d_plus)
	print(x)
