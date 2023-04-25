def doolittle(A, b):
    n = len(A)
    
    L = [[None] * n for i in range(n)]
    U = [[None] * n for i in range(n)]
    
    for i in range(n):
        for j in range(n):
            if i == j:
                L[i][j] = 1
            elif i > j:
                U[i][j] = 0
            else:
                L[i][j] = 0
    
    
    for i in range(n):
        L[i][0] = A[i][0]
        for j in range(n + 1):
            U[0][j] = A[0][j] / L[0][0]
    
    for k in range(1, n):
        for i in range(k, n):
            soma = 0
            for p in range(k):
                soma += L[i][p] * U[p][k]
            U[i][k] = A[i][k] - soma
        
        for j in range(k, n):
            soma = 0
            for p in range(k):
                soma += L[k][p] * U[p][j]
            L[k][j] = (A[k][j] - soma) / U[k][k]
            
    return L, U
    
def crout(A: list, b):
    n = len(A)
    
    for k in range(n):
        for i in range(k, n):
            soma = 0
            for t in range(k):
                soma += A[i][t] * A[t][k]
            A[i][k] = A[i][k] - soma
        for j in range(k+1, n):
            soma = 0
            for t in range(k):
                soma += A[k][t] * A[t][j]
            A[k][j] = (A[k][j] - soma) / A[k][k]
    
    # Direct substitution
    y = [0] * n
    y[0] = b[0] / A[0][0]
    for i in range(1, n):
        soma = 0
        for j in range(i):
            soma += A[i][j] * y[j]
        y[i] = (b[i] - soma) / A[i][i]
      
    # Backward substitution
    x = [0] * n
    x[-1] = y[-1]
    for i in range(n-1, -1, -1):
        soma = 0
        for j in range(i+1, n):
            soma += A[i][j] * x[j]
        x[i] = (y[i] - soma)
            
    return x


def main():
    A = [[4, 2, 3],
         [2, -4, -1],
         [-1, 1, 4]
        ]
    b = [7, 1, -5]
    
    print(crout(A, b))
    
if __name__ == '__main__':
    main()