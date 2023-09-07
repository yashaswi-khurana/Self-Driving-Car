list1=[]
len=int(input("Please Enter length of string: "))
for i in range(0,len):
    x=input("Please Enter Element ")
    list1.append(x)
print(list1)
y=input("Do You want to delete or insert:")
if(y=="delete"):
    z=input("You Want to delete by value or index or slice:")
    if(z=="value"):
        a=input("Please Enter Element to delete: ")
        list1.remove(a)
        print(list1)
    elif(z=="index"):
        a=int(input("Please Enter Index to delete: "))
        list1.pop(a)
        print(list1)
    elif(z=="slice"):
        a=int(input("Please enter start index for slicing: "))
        b=int(input("Please enter end index for slicing: "))
        list1=list1[a:b]
        print(list1)
    else:
        print("Invalid Input")
elif(y=="insert"):
    a=input("Please Enter the element you want to insert: ")
    h=int(input("Please Enter the index at which you want to insert: "))
    list1.insert(h,a)
    print(list1)
else:
    print("Invalid Input")