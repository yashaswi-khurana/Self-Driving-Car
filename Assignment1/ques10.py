x=int(input("Please enter your number:"))
list1=[]
while(x!=0):
    if(x%2==0):
        list1.append(0)
    else:
        list1.append(1)
    x=x//2
list1.reverse()
listToStr = ' '.join([str(elem) for elem in list1])
print(listToStr)
