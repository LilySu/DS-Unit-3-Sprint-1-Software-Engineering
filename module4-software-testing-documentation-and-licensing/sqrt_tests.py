def newton_sqrt(x):
    val = x
    while True:
        last = val
        val = (val + n / val) * 0.5
        if abs(val - last) < 1e-9:
            break
    return val

from numpy.testing import assert_almost_equal as eq

def newton_sqrt2(x, guess = 2):
    if eq(newton_sq2(x, guess)**2, x): 
        return guess
    else:
        guess = 0.5*(guess+x)
        return newton_sqrt2(x, guess)
    
def lazy_sqrt(x):
    return x**0.5

def builtin_sqrt(x):
    from math import sqrt
    return sqrt(x)
    
def newtons_method(f, df, x0, e):
    def dx(f, x):
        return abs(0 - f(x))
    delta = dx(f, x0)
    while delta > e:
        x0 = x0 - f(x0)/df(x0)
        delta = dx(f, x0)
    return x0