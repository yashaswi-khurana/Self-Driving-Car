uppercase = 0
lowercase = 0
digit = 0
symbols = 0
str = input("Please enter your String: ")
for i in range(len(str)):
    if str[i].isupper():
        uppercase += 1
    elif str[i].islower():
        lowercase += 1
    elif str[i].isdigit():
        digit += 1
    else:
        if str[i]==' ':
            continue
        else:
            symbols += 1
print("Number of Alphabets=",uppercase+lowercase)
print("Number of Uppercase=",uppercase)
print("Number of Lowercase=",lowercase)
print("Number of Digits=",digit)
print("Number of Symbols=",symbols)

