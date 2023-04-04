import numpy as np

def f(x):
    return np.exp(x) - 2 * np.cos(x)

def falsaPosicao(f, a, b):
    fa = f(a)
    fb = f(b)
        
    erro = 1e-15
    
    fxk = 1
    k = 0
    
    while abs(fxk) > erro:
        k += 1
        xk = a - (fa * (b - a)) / (fb - fa)
        fxk = f(xk)
        
        if fa * fxk < 0:
            b = xk
            pa = fb / (fb + fxk)
            fb = fxk
            fa = pa * fa
        else:
            a = xk
            pb = fa / (fa + fxk)
            fa = fxk
            fb = pb * fb
            
    return xk, k

def main():
    xk, k = falsaPosicao(f, 0, 2)
    print("xk =", xk)
    print("k =", k)

if __name__ == '__main__':
    main()
    