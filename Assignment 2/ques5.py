i = 1
email=[]
domain=[]
while i == 1:
    n=input("Do you want to add email id y or n:")
    if n == "y":
        email_id=input("Please enter you email id: ")
        h=email_id.split('@')
        email.append(email_id)
        domain.append(h[1])
    else:
        break

email_tuple=tuple(email)
domain_tuple=tuple(domain)

print(email_tuple)
print(domain_tuple)
