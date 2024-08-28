#p_2
n=int(input("entre a num for the range : "))
def prime_num (n):
      if n==0 or n==1:
        return False
      for i in range(2,n):
         if n%i==0:
            return False
      return True        
for i in range(1,n+1):
     if prime_num(i)==True:
        print(str(i)+" "+"is prime")
     else:
         print( str(i) +" " +"isnot a pime num")
