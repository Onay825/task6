
users = {

}
def register_user(user):
    global users
    if user in users:
       print("the user already founded ")
    else:
        users[user]=[]
        print("the user add succefully")
def send_massage (reciever,sender,msg):
    global users
    if reciever not in users or sender not in users :
          print("your request not found please try again")
    else: 
        all={
             "sender":sender ,
             "reciever":reciever ,
             "massage":msg
        }
        users[reciever].append(all)
        users[sender].append(all)
def view_massage (user_name):
    if user_name not in users  :
        print("your request not founded !")
    else:
        print(users[user_name])

        
           
        
        
    


register_user("onay")
register_user("mirna")
send_massage("onay","mirna","hello onay")
send_massage("mirna","onay","helloz mirna")
view_massage("onay")
print(users)