# Remove all occurrence of 20
list1=[5,20,15,20,25,50,20]
for elem in list1:
    if elem==20:
        list1.remove(elem)
print(list1)