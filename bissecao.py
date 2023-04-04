import math

def bipart(f, a, b):
    fa = f(a)
    fb = f(b)

    if fa == 0:
        return fa

    if fb == 0:
        return fb

    if fa * fb > 0:
        return None

    error = 1e-15

    fxm = 1
    k = 0

    while abs(fxm) > error:
        k += 1
        xm = (a + b) / 2
        fxm = f(xm)

        if fa * fxm < 0:
            b = xm
            fb = fxm
        else:
            a = xm
            fa = fxm

    return xm, k


def f(x):
    return math.exp(x) - 2 * math.cos(x)


def main():
    xm, k = bipart(f, 0, 2)
    print("xm =", xm)
    print("k =", k)


if __name__ == "__main__":
    main()
