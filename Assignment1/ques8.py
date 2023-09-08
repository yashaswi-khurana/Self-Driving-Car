vowels=['a','e','i','o','u','A','E','I','O','U']
k=input("Please enter you longest common subsequence: ")
l=len(k)
h=''
for i in k:
    if i not in vowels:
        h=h+i
    else:
        continue
k=h.split(' ')
ma=max(k,key =len)
print("This is largest subsequence: ",ma)
