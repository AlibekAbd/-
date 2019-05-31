import numpy as np
import random 
n = int(input())
A = np.random.rand(n,n)
f = np.random.rand(n)
L = np.ones_like(A)*0.0

for i in range(0,n):
	summa = 0
	for j in range(0,n):
		summa += abs(A[i][j])
	c = random.uniform(1,2)
	A[i][i] = summa + c

for i in range(n):
    for j in range(i, n):
        A[i][j] = A[j][i]

def cholesky(A):
	for i in range(n):
		for j in range(i+1):
			if i==j:
				val = A[i][i] - np.sum(np.square(L[i][i]))
				if val<0:
					return 0.0
				L[i][i] = np.sqrt(val)
			else:
				L[i][j] = (A[i][j] - np.sum(L[i][j]*L[j][j]))/L[j][j]
	return L
L = cholesky(A)

def function(A, f, n):
    x = [0] * n
    for i in range(n - 1, -1, -1):
        x[i] = f[i]
        for j in range(i + 1, n):
            x[i] = x[i] - A[i][j] * x[j]
    return np.array(x)

y = function(L, f, n)
x = function(L, y, n)
L.transpose()
print("L:",L)
print("x:",x)



				
