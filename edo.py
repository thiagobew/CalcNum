import numpy as np
import matplotlib.pyplot as plt

def f(t, y):
    return -2*t - y

def euler(f, a, b, N, y0):
    h = (b - a)/N
    
    t = np.arange(a, b+h, h)
    y = np.zeros(N+1)
    y[0] = y0
    for n in range(N):
        y[n+1] = y[n] + h*f(t[n], y[n])
        
    return t, y

def runge_kutta(f, a, b, N, y0):
    h = (b - a)/N
    
    t = np.arange(a, b+h, h)
    y = np.zeros(N+1)
    y[0] = y0
    for n in range(N):
        k1 = h*f(t[n], y[n])
        k2 = h*f(t[n] + h/2, y[n] + k1/2)
        k3 = h*f(t[n] + h/2, y[n] + k2/2)
        k4 = h*f(t[n] + h, y[n] + k3)
        
        y[n+1] = y[n] + (k1 + 2*k2 + 2*k3 + k4)/6
        
    return t, y

def main():
    x, y = runge_kutta(f, 0, 0.5, 500, -1)
    
    ye = -3*np.exp(-x) - 2*x + 2
    
    print(np.abs(ye - y))
    

if __name__ == "__main__":
    main()