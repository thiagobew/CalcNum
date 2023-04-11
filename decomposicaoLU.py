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