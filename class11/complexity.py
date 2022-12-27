import time
import sys

sys.setrecursionlimit(1000000)

def factorial(n):
    res = 1
    
    while n > 1:
        res *= n
        n -= 1

    return res

def factorial_recursive(n):
    if n == 1:
        return 1
    else:
        return n * factorial_recursive(n-1)

if __name__ == '__main__':
    n = 10000
    start = time.time()
    factorial(n)
    end = time.time()
    print(end - start)
    print('-----------------')
    start = time.time()
    factorial_recursive(n)
    end = time.time()
    print(end - start)