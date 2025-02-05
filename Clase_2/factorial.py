def factorial(n):
    if n == 1 or n==0:
        return 1
    else:
        return n * factorial(n-1)
    
x = 10
print('El resultado es: ', factorial(x))