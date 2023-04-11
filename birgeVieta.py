def birgeVerta(a: list, x: float):
    n = len(a)
    b = [None] * n
    b[0] = a[0]
    c = [None] * (n - 1)
    c[0] = b[0]

    for i in range(1, n - 1):
        b[i] = a[i] + b[i-1] * x
        c[i] = b[i] + c[i-1] * x
    b[n - 1] = b[n - 2] * x + a[n - 1]

    r = b[-1]
    r1 = c[-1]

    return r, r1


def compute(a: list, x: float):
    s = 0
    n = len(a)
    for i in range(n):
        s += a[n - 1 - i] * x ** i
    return s


def raizes(a: list):
    x = 1
    erro = 1e-16
    k = 0

    while abs(compute(a, x)) > erro:
        r, r1 = birgeVerta(a, x)
        x = x - r / r1
        k += 1

    return x, k


def main():
    p = [1, 0, 2, -1]
    x, k = raizes(p)
    print("x =", x)
    print("k =", k)


if __name__ == '__main__':
    main()
