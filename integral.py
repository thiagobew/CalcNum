import numpy as np


def f(x: float):
    return np.exp(x)


def trapezio(f: callable, a: float, b: float, n: int):
    n = int(n)

    h = (b-a)/n
    x = np.linspace(a, b, n+1)
    y = f(x)
    y_int = h / 2 * (y[0] + 2 * np.sum(y[1:-1]) + y[-1])

    return y_int


def simpson(f: callable, a: float, b: float, n: int):
    n = int(n)
    
    h = (b-a)/n
    x = np.linspace(a, b, n+1)
    y = f(x)
    y_int = h / 3 * (y[0] + 2 * np.sum(y[2:-2:2]) +
                     4 * np.sum(y[1:-1:2]) + y[-1])

    return y_int


def compute_integral(f: callable, a: float, b: float, method: str = "trapezio", start_n: int = 20):
    n = int(start_n)
    
    method_func = None
    if method == "trapezio":
        method_func = trapezio
    elif method == "simpson":
        method_func = simpson
    else:
        raise ValueError("Invalid method")
    
    y_int = method_func(f, a, b, n)
    return y_int, n
    



def main():
    print(compute_integral(f, 0, 1, "trapezio"))
    print(compute_integral(f, 0, 1, "simpson"))


if __name__ == "__main__":
    main()
