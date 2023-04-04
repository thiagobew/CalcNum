import math


def f(x):
    return math.exp(x) - 2 * math.cos(x)


def df(x):
    return math.exp(x) + 2 * math.sin(x)


def newton(x, f, df):
    error = 1
    precision = 1e-15
    k = 0
    fx = f(x)
    while (abs(error) > precision):
        k += 1
        x = x - fx / df(x)
        fx = f(x)
        error = fx
        
    return x, k


def main():
    x, k = newton(1, f, df)
    print("x =", x)
    print("k =", k)

if __name__ == '__main__':
    main()