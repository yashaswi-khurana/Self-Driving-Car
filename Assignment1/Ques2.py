size1=int(input('Please enter the size of the first list: '))
list1=[]
for i in range(size1):
    elem=input('Please enter your element:')
    list1.append(elem)
size2=int(input('Please enter the size of the second list: '))
list2=[]
for i in range(size2):
    elem=input('Please enter your element:')
    list2.append(elem)
list3=list(list1+list2)
print(list3)