m1,n1=map(str,input().split())
r1=len(m1)
p1=0
for i in range(r1):
    if(m1[i]!=n1[i]):
        p1=p1+1
if(p1==1):
    print("yes")
else:
    print("no")
