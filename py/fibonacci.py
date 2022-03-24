# 0 1 1 2 3 5 8 13 21  fibonacani number



def fibo1(n):
    if n==1:
        return 0

    elif n==2:
        return 1

    else:
        return fibo1(n-1)+ fibo1(n-2)

num = int(input("enter the number "))
print(fibo1(num))
