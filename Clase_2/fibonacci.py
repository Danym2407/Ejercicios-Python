def fibonacci(n):
    if(n>2):
        return fibonacci(n-1) + fibonacci(n-2)
    elif(n==2):
        return 1
    elif(n==1):
        return 1
    elif(n==0):
        return 0
    
    
fibo = int(input("Ingresa que numero de fibonacci deseas ver: "))

for i in range(0, fibo):
    print('Resultado es: ', fibonacci(i))