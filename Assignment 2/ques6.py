def function():
    str= input("Please enter your string: ")
    lst1= str.split(" ")
    for elem in lst1:
            if (elem=="Dog" or elem=="dog"):
                return True
    return False
print(function())
