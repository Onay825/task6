TOTAL_purchase= float (input("Entre the total purchase amount: "))
years_being_mem= float (input("Entre how many years have you been a member in the library: "))
complains= float (input("Entre how many times have you made a complains: "))
purchase= float (input("Entre how many purchase have you done: "))
x=0
if years_being_mem>10:
    x+=(10/100)
elif years_being_mem>=6 or years_being_mem<=10:
    x+=(8/100)
elif years_being_mem<6:
    x+=(5/100)
while complains>0:
    x-=(2/100)
    complains-=1
if x<0:
    x=0
if purchase>=20:
    x+=(5/100)
NET_DISCOUNT=TOTAL_purchase*x
TOTAL_purchase=TOTAL_purchase-NET_DISCOUNT
print(NET_DISCOUNT)
print(TOTAL_purchase)