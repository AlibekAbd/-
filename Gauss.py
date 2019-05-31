import numpy as np
import random
import scipy.linalg as sla
n = int(input())
A = np.random.rand(n,n)
f = np.random.rand(n)

#diagonal dimension
for i in range(0,n):
	summa = 0
	for j in range(0,n):
		summa += abs(A[i][j])
	c = random.uniform(1,2)
	A[i][i] = summa + c
	
def forward_elimination(A, f, n):
	for k in range(0, n-1):
		for i in range(k+1, n):
			t = A[i][k] / A[k][k]
			for j in range(k, n):
				A[i][j] -=  t * A[k][j]
			f[i] -=  t * f[k]
	return A, f
	
def backward_substitution(a, b, n):
	x = [0] * n
	x[n-1] = f[n-1] / a[n-1][n-1]
	for k in range(n-2, -1, -1):
		summa = f[k]
		for j in range(k+1, n):
			summa -=  a[k][j] * x[j]
		x[k] = summa / a[k][k]
	return np.array(x)

A, f = forward_elimination(A, f, n)
x = backward_substitution(A, f, n)
#y = np.linalg.solve(A,f)
#print("y = ",y)
print("x = ",x)
	
