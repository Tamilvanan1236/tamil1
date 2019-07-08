a,b=list(map(int,input().split()))
r=n=0
for i in range(a+1,b):
    n=0
    j=i
    while i!=0:
        r=i%10
        n=n+(r*r*r)
        i=i//10
    if j==n:
        print(n,end=' ')
