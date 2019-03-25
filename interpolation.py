import numpy as np
import matplotlib.pyplot as plt

def coef(x, y):
    '''x : array of data points
       y : array of f(x)  '''
    x.astype(float)
    y.astype(float)
    n = len(x)
    a = []
    for i in range(n):
        a.append(y[i])

    for j in range(1, n):

        for i in range(n-1, j-1, -1):
            a[i] = float(a[i]-a[i-1])/float(x[i]-x[i-j])

    return np.array(a) # return an array of coefficient

def Eval(a, x, r):

     ''' a : array returned by function coef()
        x : array of data points
        r : the node to interpolate at  '''
    x.astype(float)
    n = len( a ) - 1
    temp = a[n]
    for i in range( n - 1, -1, -1 ):
        temp = temp * ( r - x[i] ) + a[i]
    return temp # return the y_value interpolation

if __name__ == "__main__":
    Eval([0  ,1 , 2,  5.5,  11,  13,  16,  18], [0.5 ,3.134 ,5.9 ,9.9 ,10.2 ,9.35 ,7.2 ,6.2], 8)
