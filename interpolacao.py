import numpy as np
import matplotlib.pyplot as plt
import random


def plot(x_real: list, y_real: list, res):
    plt.scatter(x_real, y_real, color='red')

    plt.xticks(x_real)

    x = np.linspace(min(x_real), max(x_real), 1000)

    y = [sum([res[i] * x[j]**i for i in range(len(res))])
             for j in range(len(x))]

    plt.plot(x, y, color='blue')
    plt.show()


def interpolate(x_real, y_real):
    n = len(x_real)

    A = [[0 for i in range(n)] for j in range(n)]
    b = [0 for i in range(n)]

    for i in range(n):
        for j in range(n):
            A[i][j] = x_real[i]**j
        b[i] = y_real[i]

    res = np.linalg.solve(np.array(A), np.array(b))

        
        
    return res, n

def lagrange(x, y, xx):
    n = len(x)    
    px = 0
    
    for i in range(n):
        num = 1
        dem = 1
        for j in range(n):
            if i != j:
                num *= xx - x[j]
                dem *= x[i] - x[j]
        
        px += y[i] * num / dem
                
    return px

def generate_points_lagrange(x, y, n):
    new = []
    
    for i in range(n):
        new_x = random.uniform(min(x), max(x))
        new_y = lagrange(x, y, new_x)
        new.append((new_x, new_y))
    
    new.sort(key=lambda x: x[0])
    
    return [i[0] for i in new], [i[1] for i in new]

def plot_lagrange(x_real, y_real, x_lagrange, y_lagrange):
    plt.scatter(x_real, y_real, color='red')
    plt.xticks(x_real)
    plt.plot(x_lagrange, y_lagrange, color='blue')
    plt.show()

def main():
    x = [-1, 0, 1]
    y = [4, 1, -1]
    
    #x = [random.uniform(0, 100) for i in range(20)]
    #y = [random.uniform(0, 100) for i in range(20)]
    
    #res, nterms = interpolate(x, y)
    x_la, y_la = generate_points_lagrange(x, y, 100)

    #plot(x, y, res)
    plot_lagrange(x, y, x_la, y_la)

if __name__ == '__main__':
    main()