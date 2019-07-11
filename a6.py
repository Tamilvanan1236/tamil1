a1,a2=map(int,input().split())
a3=[]
for i in range(a1,a2+1):
    for j in range(2,i):
        if(i%j==0):
            break
    else:
        a3.append(i)
print(len(a3))
