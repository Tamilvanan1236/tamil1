s1=input()
s1=s1.split()
s1=list(map(int,s1))
t1=int(s1[0])
f1=int(s1[1])
l=[]
for i in range(t1,f1+1):
    if(i>1):
        for j in range(2,i):
            if(i%j==0):
               break
        else:
           l.append(i)
print(*l,sep=" ")
      
