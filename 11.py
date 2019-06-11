g=input()
g=g.split()
z1=int(g[0])
z2=int(g[1])
q=input()
q=q.split()
d=0
l1=[]
l2=[]
for i in g:
    l1.append(int(i))
for j in q:
    l2.append(j)
if(z2<=z1):
    for i in range(0,z2):
        d=d+int(l2[i])
print(d)
        
