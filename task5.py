#p_1
num=int(input("entre your target num: "))
x=0
y=1
z=0
if num==1:
     print(x)
elif num==2:
     print(y)
else:
      for i in range(num-2):
        z=x+y
        x=y
        y=z
      print(z)


    