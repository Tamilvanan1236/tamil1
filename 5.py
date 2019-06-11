q=input()
q=q.split()
if(q[0]>q[1] and q[0]>q[2]):
    print(q[0])
elif(q[1]>q[0] and q[1]>q[2]):
    print(q[1])
else:
    print(q[2])
