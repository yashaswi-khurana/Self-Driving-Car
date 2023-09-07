inp=input("Please enter you numbers separated by spaces: ")
list1=inp.split()
for i in range(len(list1)):
    list1[i]=int(list1[i])
list2=[]
for i in range(len(list1)):
    x=min(list1)
    list2.append(x)
    list1.remove(x)
list1=list2
print(list1)