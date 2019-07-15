a1,a2=input().split()
a3=abs(len(a1)-len(a2))
for i in range(0,len(a1)):
    if(a1[i]!=a2[i]):
        a3+=1
print(a3)
        
