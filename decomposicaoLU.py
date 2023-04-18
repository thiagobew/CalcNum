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
    
def crout(A, b):
    n = len(A)
    
    L = [[None] * n for i in range(n)]
    U = [[None] * n for i in range(n)]
    
    for i in range(n):
        for j in range(n):
            if i == j:
                U[i][j] = 1
            elif i > j:
                U[i][j] = 0
            else:
                L[i][j] = 0


def main():
    A = []
    b = []
    
    doolittle(A, b)
    
if __name__ == '__main__':
    main()