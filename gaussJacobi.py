import numpy as np
import random

def gauss_jacobi(A, b, x0, max_iterations=1000, tol=1e-6):
    n = len(b)
    x = x0.copy()
    for k in range(max_iterations):
        x_new = np.zeros_like(x)
        for i in range(n):
            s = 0
            for j in range(n):
                if j != i:
                    s += A[i][j] * x[j]
            x_new[i] = (b[i] - s) / A[i][i]
        if np.linalg.norm(x_new - x) < tol:
            return x_new
        x = x_new
    raise Exception("Gauss-Jacobi method did not converge")

def main():
    size = 3
    
    A = [[random.random() * 1 for i in range(size)] for j in range(size)]
    
    b = [random.random() * 1 for i in range(size)]
    
    gauss_jacobi(A, b, np.zeros(size))

if __name__ == '__main__':
    main()