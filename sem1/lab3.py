import numpy as np
import lab2

def simplex_method_init(c, A, b):
	m = len(A)
	n = len(A[0])
	# step 1
	A[b < 0] *= -1
	b[b < 0] *= -1

	# step 2
	c_help = np.concatenate((np.zeros(n), np.full(m, -1)))
	A_help = np.hstack((A, np.eye(m)))

	# step 3
	x_help = np.concatenate((np.zeros(n), b))
	B = np.array([i for i in range(n, m+n)])

	# step 4
	x_help, B = lab2.simplex_method(A_help, c_help, b, x_help, B)

	# step 5
	if np.any(x_help[n:m+n] != 0):
		raise Exception('задача несовместна')

	# step 6
	x = x_help[:n]

	while np.max(B) >= n:

		j_k = np.max(B)
		k = np.where(B == j_k)

		A_B_inv = np.linalg.inv(A_help[:, B])

		replaced = False
		for j in np.setdiff1d(np.arange(n), B):
			# step 7
			l = A_B_inv @ A[:, j]
			# step 8
			if l[k] != 0:
				replaced = True
				B[j_k] = j
				break

		# step 9
		if not replaced:
			i = j_k - n
			A = np.delete(A, i, axis=0)
			b = np.delete(b, i, axis=0)
			B = np.delete(B, k, axis=0)
			A_help = np.delete(A_help, i, axis=0)

	return x, B, A, b

if __name__ == '__main__':
	A = np.array([
		[1, 1, 1],
		[2, 2, 2],
	])
	c = np.array([1, 0, 0])
	b = np.array([0, 0])

	x, B, A, b = simplex_method_init(c, A, b)
	print('x = ', x)
	print('B = ', B)
	print('A = ', A)
	print('b = ', b)
