import random

def gauss_elimination(A, b):
    """
    Solves the system of linear equations Ax = b using Gaussian elimination.
    Returns the solution vector x.
    """
    n = len(A)

    # Augment the matrix A with the column vector b
    Ab = [A[i] + [b[i]] for i in range(n)]

    
    # Forward elimination
    for i in range(n):
        # Find the row with the largest absolute valu# Find the row with the largest absolute value in column i
        max_row = i
        for j in range(i+1, n):
            if abs(Ab[j][i]) > abs(Ab[max_row][i]):
                max_row = j
        # Swap the max row with the current row i
        Ab[i], Ab[max_row] = Ab[max_row], Ab[i]
        # Eliminate the variable in column i for all rows below row ie in column i
        max_row = i
        for j in range(i+1, n):
            if abs(Ab[j][i]) > abs(Ab[max_row][i]):
                max_row = j
        # Swap the max row with the current row i
        Ab[i], Ab[max_row] = Ab[max_row], Ab[i]
        # Eliminate the variable in column i for all rows below row i
        for j in range(i+1, n):
            factor = Ab[j][i] / Ab[i][i]
            for k in range(i+1, n+1):
                Ab[j][k] -= factor * Ab[i][k]

    # Backward substitution
    x = [0] * n
    for i in range(n-1, -1, -1):
        x[i] = Ab[i][n] / Ab[i][i]
        for j in range(i-1, -1, -1):
            Ab[j][n] -= Ab[j][i] * x[i]

    return x

def no_pivot(A, b):
    n = len(A)
    
    for k in range(n - 1):
        for i in range(k + 1, n):
            factor = A[i][k] / A[k][k]
            b[i] -= b[k] * factor
            for j in range(k, n):
                A[i][j] -= A[k][j] * factor
                
    # Backward substitution
    x = [0] * n
    for i in range(n-1, -1, -1):
        x[i] = b[i] / A[i][i]
        for j in range(i+1, n):
            x[i] -= A[i][j] * x[j] / A[i][i]
            
    return x

def partial_pivot(A, b):
    n = len(A)
    
    # index vector for changing the order of the rows
    o = [i for i in range(n)]
    
    for k in range(n - 1):
        # Find the row with the largest absolute value in column i
        max_row = k
        for j in range(k+1, n):
            if abs(A[o[j]][k]) > abs(A[o[max_row]][k]):
                max_row = j
        
        o[k], o[max_row] = o[max_row], o[k]
        
        for i in range(k + 1, n):
            factor = A[o[i]][k] / A[o[k]][k]
            b[o[i]] -= b[o[k]] * factor
            for j in range(k, n):
                A[o[i]][j] -= A[o[k]][j] * factor
                
    # Backward substitution
    x = [0] * n
    for i in range(n-1, -1, -1):
        x[i] = b[o[i]] / A[o[i]][i]
        for j in range(i+1, n):
            x[i] -= A[o[i]][j] * x[j] / A[o[i]][i]
    
    print(o)
    return x

def main():
    ''' A = [
        [1, -1, 1],
        [2, 3, -1],
        [-3, 1, 1]
    ]
    
    b = [1, 4, -1] '''
    
    size = 100
    
    A = [[random.randint(1, 10) for i in range(size)] for j in range(size)]
    
    b = [random.randint(1, 10) for i in range(size)]
    
    print(partial_pivot(A, b))

if __name__ == "__main__":
    main()
    