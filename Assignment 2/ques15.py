N= int(input("Please enter value of n: "))
x=0
y=2
z=10
ans=0
for i in range(N):
    x+=(z**i)*y
    ans+=x
print(ans)
