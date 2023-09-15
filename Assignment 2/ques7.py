def function():
    str= input("Please enter your string: ")
    lst1= str.split(" ")
    count=0
    for elem in lst1:
            if (elem=="Dog" or elem=="dog" or elem=="dog." or elem=="Dog."):
                count+=1
    return count
count = function()
if(count==0):
    print("Dog not present in function")
else:
    print(count)