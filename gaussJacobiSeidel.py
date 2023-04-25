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
        
        print(x_new)
        if np.linalg.norm(x_new - x) <= tol:
            return x_new
        x = x_new
    raise Exception("Gauss-Jacobi method did not converge")


def gauss_seidel(A, b, x0, max_iterations=1000, tol=1e-6):
    n = len(b)
    x = x0.copy()
    for k in range(max_iterations):
        x_new = np.zeros_like(x)
        for i in range(n):
            s = 0
            for j in range(i):
                s += A[i][j] * x_new[j]

            for j in range(i + 1, n):
                s += A[i][j] * x[j]

            x_new[i] = (b[i] - s) / A[i][i]

        print(x_new)
        if np.linalg.norm(x_new - x) <= tol:
            return x_new
        x = x_new
    raise Exception("Gauss-Seidel method did not converge")


def main():
    A = np.array(
        [[3, -1, -1],
         [1, 3, 1],
         [2, -2, 4]]
    )
    b = np.array([1, 5, 4])

    print(gauss_seidel(A, b, [0] * len(b), 100, 1e-16))


if __name__ == '__main__':
    main()
