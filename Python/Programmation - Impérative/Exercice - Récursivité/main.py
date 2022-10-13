def add(n):
    if n == 0:
        return 0
    else:
        return n + add(n-1)

def zero(n):
    if n%10 == 0:
        return True
    elif n < 10:
        return False
    else:
        return zero(n//10) 

def puissance(x,n):
    if n == 0:
        return 1
    else:
        if n > 0:
            return x * puissance(x, n-1)
        else: 
            return puissance(x,n+1)/x

def fibonacci(n):
    if(n==0):
        return 0
    if(n == 1):
        return 1
    return (fibonacci(n-1) + fibonacci(n-2))

if __name__ == '__main__':
    print(fibonacci(30))
    print(add(2))
