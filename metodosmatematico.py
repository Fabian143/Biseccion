from decimal import Decimal, getcontext
import math

#primera función x a la x
def f1(x):
    return x**x

#función que busca distintas aproximaciones
def f(x,n):
    match n:
        case 1:
            #aproximación de x a la x=7
            return f1(x) - Decimal(7)

def errorabsoluto(xn,xa):
    return abs((xn-xa)/xn)*100
