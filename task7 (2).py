def fibonacci_num (n):
    x=0
    y=1
    if n < 0:
        print("incorrect input")
    elif n==0:
        return x
    elif n==1 or n==2:
        return y
    else :
        for i in range(2,n):
            z = x+y
            x = y
            y = z
        return z
print(fibonacci_num(2))