import numpy as np

n = int(input())
A = np.ones((n,n)) *0.0
a = np.random.sample(n)
b = np.random.sample(n)
c = np.random.sample(n)
f = np.random.sample(n)

def progonka(a,b,c,f,n):
	alpha = np.array([0.0] * (n + 1))
	beta = np.array([0.0] * (n + 1))
	a[1] = 0
	c[1] = 0
	alpha[1] = 0
	beta[1] = 0
	x = np.array([0.0] * n)
	for i in range(n-1):
		d = a[i+1] * alpha[i] + b[i+1]
		alpha[i+1] =  - c[i+1] / d
		beta[i+1] = (f[i+1] - a[i+1] * beta[i]) / d
	x[n-1] = beta[n-1]
	for i in range(n - 2, -1, -1):
		x[i] = alpha[i] *x[i+1] + beta[i]
	return x
	
x = progonka(a, b, c, f, n)
print(x)
