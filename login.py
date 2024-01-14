# A simple authentication code

#db
user = "anouar"
passwd = 12345
#ask users
# check input with db
valid_cred = False
while not valid_cred:
    ask = input("Enter your Name: ")
    ask_pass = int(input("Enter your Password: "))
    if user == ask and passwd == ask_pass:
       print(f"Welcome back {ask}")
       valid_cred = True
    else:
       print(f"this Name is not in our database, try register please")