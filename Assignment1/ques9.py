password=input("Please enter you Password: ")
lower=0
upper=0
for i in password:
    if('a'<=i<='z'):
        lower+=1
    elif('A'<=i<='Z'):
        upper+=1    
if len(password)<6:
    print("Password is too short")
if '&' not in password:
    print("Password must contain symbol &")
if (lower==0 or upper==0):
    print("Password must contain atleast one upper and lower case letter")

