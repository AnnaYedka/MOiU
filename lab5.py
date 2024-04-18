import numpy as np
from collections import Counter


def matrix_transport_task(a, b, C):
	# find first basis
	m, n = np.shape(C)
	X = np.zeros((m, n))
	B = []

	i, j = 0, 0
	while i < m and j < n:
		B.append((i, j))
		if a[i] >= b[j]:
			X[i][j] = b[j]
			a[i] -= b[j]
			j += 1
		else:
			X[i][j] = a[i]
			b[j] -= a[i]
			i += 1

	while True:
		# calculate the potentials
		B.sort(key=lambda tup: tup[0])
		u = {0: 0}
		v = {}

		def calculate_potentials(B):
			leaves = []
			for i, j in B:
				if u.get(i) is not None:
					v[j] = C[i][j] - u[i]
				elif v.get(j) is not None:
					u[i] = C[i][j] - v[j]
				else:
					leaves.append((i, j))
			if len(leaves) > 0:
				calculate_potentials(leaves)

		calculate_potentials(B)

		# check plan if optimal
		additional_pos = None
		is_optimal = True
		for i in range(m):
			for j in range(n):
				if u[i] + v[j] > C[i][j]:
					is_optimal = False
					additional_pos = (i, j)
					B.append((i, j))
					break
			if additional_pos is not None:
				break
		if is_optimal:
			return X, B

		# find corner nodes
		B_copy = B.copy()
		while True:
			i_count = Counter([i for (i, _) in B_copy])
			j_count = Counter([j for (_, j) in B_copy])
			i_rm = [i for i in i_count if i_count[i] == 1]
			j_rm = [j for j in j_count if j_count[j] == 1]

			if not i_rm and not j_rm:
				break
			B_copy = [(i, j) for i, j in B_copy if i not in i_rm and j not in j_rm]

		# sign nodes, find theta
		B_copy.pop()
		plus = [additional_pos]
		minus = []
		sign_plus = False
		curr_pos = additional_pos
		theta = float('inf')
		theta_pos = ()

		while B_copy:
			for ind, (i, j) in enumerate(B_copy):
				if curr_pos[0] == i or curr_pos[1] == j:
					curr_pos = (i, j)
					B_copy.pop(ind)
					if sign_plus:
						plus.append((i, j))
						sign_plus = False
					else:
						minus.append((i, j))
						sign_plus = True
						if X[i][j] < theta:
							theta_pos = (i, j)
							theta = X[i][j]
					break
		B.remove(theta_pos)

		for i, j in plus:
			X[i][j] += theta

		for i, j in minus:
			X[i][j] -= theta


if __name__ == "__main__":
	# C = np.array([
	# 	[8, 4, 1],
	# 	[8, 4, 3],
	# 	[9, 7, 5]
	# ])
	#
	# a = np.array([100, 300, 300])
	# b = np.array([300, 200, 200])

	C = np.array([
		[3, 20, 8, 13, 4, 100],
		[4, 4, 18, 14, 3, 0],
		[10, 4, 18, 8, 6, 0],
		[7, 19, 17, 10, 1, 100]
	])

	a = np.array([80, 60, 30, 60])
	b = np.array([10, 30, 40, 50, 70, 30])

	X, B = matrix_transport_task(a, b, C)
	print(X)
