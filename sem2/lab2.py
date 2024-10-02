import numpy as np
from sem1.lab3 import simplex_method_init
from sem1.lab2 import simplex_method


def simplex_method_full(c, A, b):
	x, B, A, b = simplex_method_init(c, A, b)
	return simplex_method(A, c, b, x, B)


def gomory(c, A, b):
	# step 1
	x, B = simplex_method_full(c, A, b)
	# step 2, 3
	if all(val.is_integer() for val in x):
		return x
	# step 4, 5
	i = 0
	while x[i].is_integer():
		i += 1
	k = 0
	while B[k] != i:
		k += 1

	# step 6, 7
	n = len(x)
	A_B = A[:, B]
	not_B = np.setdiff1d(range(n), B)
	A_N = A[:, not_B]

	# step 8
	A_B_inv = np.linalg.inv(A_B)

	# step 9
	Q = A_B_inv @ A_N

	# step 10
	l = Q[k]

	# step 11
	print(' + '.join([f'{l[p] % 1}x{not_B[p]}' for p in range(len(l))]), f' - x{n} = {x[i] % 1}')

	res = np.zeros((n + 1))
	for i in range(len(not_B)):
		res[not_B[i]] = l[i]
	res[-1] = -1
	return res, x[i] % 1


if __name__ == "__main__":
	c = np.array([0, 1, 0, 0])
	b = np.array([6, 0])
	A = np.array([
		[3, 2, 1, 0],
		[-3, 2, 0, 1]
	])
	l, x = gomory(c, A, b)
	print('Вектор коэффициентов при переменных: ', l)
	print('Свободный член: ', x)
