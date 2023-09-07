vowels=['a','e','i','o','u','A','E','I','O','U']
k=input("Please enter you longest common subsequence: ")
l=len(k)
h=''
for i in k:
    if i not in vowels:
        h=h+i
    else:
        continue
print("The longest common subsequence without vowels is:",h)