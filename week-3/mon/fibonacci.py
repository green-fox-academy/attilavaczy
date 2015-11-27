#R(0) = 0
#R(1) = 1
#R(n) = R(n-1) + R (n-2)

def fibo(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return (fibo(n-1) + fibo(n-2))
print (fibo(5))

#fibo(0) => 0
#fibo(1) => 1
#fibo(2) => 1
#fibo(3) => 2
