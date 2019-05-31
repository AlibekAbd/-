import numpy as np 
from scipy.linalg import solve_banded
N = int(input())
B = np.ones((3,N)) * 0.0
a = np.random.rand(N)
b = np.random.rand(N)
c = np.random.rand(N)
d = np.random.rand(N)
a[0], c[N - 1] = 0, 0
b[0] = abs(a[0]) + abs(b[0]) + abs(c[0]) + 1
for i in range(N-1):
    b[i] = abs(a[i]) + abs(b[i]) + abs(c[i]) + 1
    B[0][i+1]=c[i]
    B[1][i]=b[i]
    B[2][i]=a[i+1] 
x = solve_banded((1, 1), B, d)
print(x)
