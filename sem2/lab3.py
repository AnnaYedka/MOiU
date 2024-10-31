import numpy as np

def resource_distribution(A):
	P, Q = len(A), len(A[0])

	B = np.zeros((P, Q), dtype=int)
	C = np.zeros((P, Q), dtype=int)
	B[0] = A[0]
	C[0] = [i for i in range(Q)]

	for p in range(1, P):
		for q in range(1, Q):
			for i in range(q+1):
				a = A[p][i]
				b = B[p-1][q-i]
				val = a + b
				if val > B[p][q]:
					B[p][q] = val
					C[p][q] = i

	res = np.zeros((P,), dtype=int)
	p = P-1
	q = Q-1
	while p >= 0:
		res[p] = C[p][q]
		q -= C[p][q]
		p -= 1

	return B[P-1][Q-1], res


if __name__ == "__main__":
	A = np.array([
		[0, 1, 2, 3],
		[0, 0, 1, 2],
		[0, 2, 2, 3],
	])

	print(resource_distribution(A))
