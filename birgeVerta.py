def birgeVerta(a: list, x: float):
	n = len(a)
	b = [None] * n
	b[0] = a[0]
	c = [None] * n
	c[0] = b[0]
	for i in range(1, n - 1):
		b[i] = a[i] + b[i-1] * x
		c[i] = b[i] + c[i-1] * x
	b[n] = b[n-1] * x + a[n]
	c[n] = b[n-1] * n + b[n]
 
	r = b[-1]
	r1 = c[-1]
	
	return r, r1

def raizes(a: list):
    x = 1
    erro = 1e-8
    k = 0
    
    while abs(x) > erro:
        r, r1 = birgeVerta(a, x)
        x = x - r / r1
        k += 1
        
    return x, k

p = [1, 0, 2, -1]
print(raizes(p))
		