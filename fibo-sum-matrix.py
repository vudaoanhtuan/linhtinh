from pwn import * 
import numpy as np
from numpy.core.numeric import concatenate, isscalar, binary_repr, identity, asanyarray, dot
from numpy.core.numerictypes import issubdtype    
from gmpy2 import mpz


def matrix_power(M, n, mod_val):
    # Implementation shadows numpy's matrix_power, but with modulo included
    M = asanyarray(M)
    if len(M.shape) != 2 or M.shape[0] != M.shape[1]:
        raise ValueError("input  must be a square array")
    # if not issubdtype(type(n), int):
    #     raise TypeError("exponent must be an integer")

    from numpy.linalg import inv

    if n==0:
        M = M.copy()
        M[:] = identity(M.shape[0])
        return M
    elif n<0:
        M = inv(M)
        n *= -1

    result = M % mod_val
    if n <= 3:
        for _ in range(n-1):
            result = dot(result, M) % mod_val
        return result

    # binary decompositon to reduce the number of matrix
    # multiplications for n > 3
    beta = binary_repr(n)
    Z, q, t = M, 0, len(beta)
    while beta[t-q-1] == '0':
        Z = dot(Z, Z) % mod_val
        q += 1
    result = Z
    for k in range(q+1, t):
        Z = dot(Z, Z) % mod_val
        if beta[t-k-1] == '1':
            result = dot(result, Z) % mod_val
    return result % mod_val




def powmod(A, n, N):
    if n == 1:
        return A
    elif n==2:
        return np.dot(A,A)
    else:
        return np.dot(A,A).dot(A)
    t = powmod(A, n/4, N)
    s = np.dot(t,t)
    s = np.dot(s,s)
    if n % 4 == 0:
        return s
    elif n%4==1:
        return s.dot(A)
    elif n%4==2:
        return s.dot(A).dot(A)
    else:
        return s.dot(A).dot(A).dot(A)

def g(n, N):
    a = np.array([[mpz(0),mpz(1),mpz(1),mpz(1)], [mpz(1),mpz(0),mpz(0),mpz(0)], [mpz(0),mpz(1),mpz(0),mpz(0)], [mpz(0),mpz(0),mpz(1),mpz(0)]])
    t = matrix_power(a,n,N)
    return t
    # return np.linalg.matrix_power(a, n) % N
 

def fibo(n, N):
    v = np.array([mpz(4),mpz(1),mpz(2),mpz(3)])
    A = g(n-4, N)
    t = np.dot(A,v)
    return t[0] % N

# f = open("fibo.txt", "w")
# for i in range(1000000):
#     f.write(str(fibo(i)) + "\n")

# f.close()

host, port = '35.200.176.244', 8856

r = remote(host, port) 

for i in range(1000):
    print r.readuntil('n=')
    n = r.readline() 
    n = int(n) 

    print r.readuntil('N=')
    N = r.readline() 
    N = int(N) 

    temp = fibo(n,N)
    r.writeline('{}'.format(temp))
    
    print temp 
    print N 
    print n 
    print '='*10, i 
    if i == 99:
        print r.readline()
        break