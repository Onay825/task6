#task-4_problem_1
if __name__ == '__main__':
    o=int(input("entre your dgree out of 100:"+" "))
    if o>=90:
        print("A")
    elif o>=80:
        print("B")
    elif o >=70:
        print("c")
    elif o>=60:
        print("D")
    elif o<=59:
        print("F")
    else:
        print("hard luck")
#task_4_problem_2
    num_1=int(input("entre the frist num"))
    operator = input("entre a operator: ")
    num_2=int(input("entre the second num"))
    if operator=="-":
       print( num_1-num_2)
    elif operator=="*":
        print(num_1*num_2)
    elif operator=="/":
        print(num_1/num_2)
    elif operator=="+":
       print( num_1+num_2)
    elif operator=="%":
      print (num_1%num_2)
    else:
        print("your requset isnot found see you in the next update")



