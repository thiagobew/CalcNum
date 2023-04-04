import math


def f(x):
    return math.exp(x) - 2 * math.cos(x)

def secante(x, f):
    error = 1
    precision = 1e-15
    k = 0
    
    xprev = 0
    if x == xprev:
        xprev = x + 1e-15
    
    fx = f(x)
    while (abs(error) > precision):
        k += 1
        x = x - (x - xprev) * fx / (fx - f(xprev))
        fx = f(x)
        error = fx
        
    return x, k


def main():
    x, k = secante(0, f)
    print("x =", x)
    print("k =", k)

if __name__ == '__main__':
    main()