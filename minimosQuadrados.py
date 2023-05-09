import numpy as np
import matplotlib.pyplot as plt
import random
from enum import Enum

class Type(Enum):
    POLYNOMIAL = 1
    EXPONENCIAL = 2


def plot(x_real, y_real, res, type: Type = Type.POLYNOMIAL):
    plt.scatter(x_real, y_real, color = 'red')
    
    x = np.linspace(min(x_real), max(x_real), 1000)
    
    if type == Type.POLYNOMIAL:
        y = [sum([res[i] * x[j]**i for i in range(len(res))]) for j in range(len(x))]
    elif type == Type.EXPONENCIAL:
        y = [res[0] * np.exp(res[1] * x[i]) for i in range(len(x))]
    
    plt.plot(x, y, color = 'blue')
    plt.show()

def error(x_real, y_real, res):
    y = [sum([res[i] * x_real[j]**i for i in range(len(res))]) for j in range(len(x_real))]
    return sum([(y_real[i] - y[i])**2 for i in range(len(y))])

def polinomial(x_real, y_real, M):
    n = len(x_real)
    
    A = [[0 for i in range(M + 1)] for j in range(M + 1)]
    b = [0 for i in range(M + 1)]
    
    for i in range(M + 1):
        for j in range(M + 1):
            if i <= j:
                A[i][j] = sum([x_real[k]**(i + j) for k in range(n)])
            else:
                A[i][j] = A[j][i]
        b[i] = sum([y_real[k] * x_real[k]**i for k in range(n)])
    
    return np.linalg.solve(np.array(A), np.array(b))

def exponencial(x_real, y_real):
    n = len(x_real)
    
    A = [[0, 0], [0, 0]]
    b = [0, 0]
    
    A[0][0] = n
    A[0][1] = sum([x_real[i] for i in range(n)])
    A[1][0] = A[0][1]
    A[1][1] = sum([x_real[i]**2 for i in range(n)])
    
    b[0] = sum([np.log(y_real[i]) for i in range(n)])
    b[1] = sum([x_real[i] * np.log(y_real[i]) for i in range(n)])
    
    res = np.linalg.solve(np.array(A), np.array(b))
    return [np.exp(res[0]), res[1]]

def main():
    
    x = [1.3, 3.4, 5.1, 6.8, 8]
    y = [2, 5.2, 3.8, 6.1, 5.8]
    
    #x = [random.uniform(0, 100) for i in range(50)]
    #y = [random.uniform(0, 100) for i in range(50)]
    
    M = 2

    res = exponencial(x, y)
    print(error(x, y, res))
    plot(x, y, res, Type.EXPONENCIAL)

if __name__ == '__main__':
    main()