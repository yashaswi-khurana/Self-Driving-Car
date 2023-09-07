x=input("Please Input Your string:")
# y=x.title()
# print(y)
j=''
y=x.split()
for word in y:
    h=word.capitalize()
    j=j+h+' '
print(j)   


