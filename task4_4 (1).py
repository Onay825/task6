age=int(input("Entre your age: "))
Reasons=""
loan=int(input("Entre the loan amount: "))
Monthly_income=float(input("Entre your monthly income: "))
Employment_statue=str(input("Entre your employment(employed/unemployed): "))
Outing_loans= str(input("Do you have any outstandind loans?(yes/no)"))
Credit_score=int(input("Entreyour cridet score:"))
print(age,loan,Monthly_income,Employment_statue,Outing_loans,Credit_score)
if age<18:
    Reasons+= "you arenot old enough"
if Monthly_income<loan/12:
    Reasons+= "Insufficient income "
if Employment_statue!= "employed":
    Reasons+="Unemployed"
if Credit_score<=350 and Credit_score>=800:
    Reasons+= "your cridet score is not accepted"
if Outing_loans== "NO":
    Reasons+="you donot have Out side loans"
if Reasons=="":
    print("Congratulations:your are succed")
else:
    print("sorry your request unaccepted"+ " "+"Reasons: "+Reasons)

