di={'a':100,'b':200,'c':300}
for i in di:
    if(di[i]==200):
        print("Value found at:",i)
        break
else:
    print("Value not found")