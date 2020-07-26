#!/usr/bin/python3
# (\sum_{i=1}^{n} i)^2 - \sum_{i=1}^{n} i^2

def square(i):
    """squares i"""
    return i*i

def sumOnetoN(n):
    """sum from 1 to n"""
    result = 0
    for i in range(1,n+1):
        result += i
    return result

def sumOne2toN2(n):
    """sum from 1^2 to n^2"""
    result = 0
    for i in range(1,n+1):
        result += square(i)
    return result

if __name__ == '__main__':
    n = 10
    answer = sumOne2toN2(n) - square(sumOnetoN(n))
    print(answer)

    # or..
    print(sum([ i**2 for i in range(1,n+1) ],0) - sum([ i for i in range(1,n+1) ],0)**2)
    # or..
    print(n*(n+1)*(2*n+1)/6 - (n*(n+1)/2)**2)
